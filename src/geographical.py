# Copyright 2025 ntskwk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import geopandas as gpd
from geopandas import GeoDataFrame


def geographical_comparison(
    new_gdf: GeoDataFrame, old_gdf: GeoDataFrame, tolerance: float = 0.1
) -> GeoDataFrame:
    """
    使用地理相交合并两个GeoDataFrame

    Args:
        new_gdf: 新的GeoDataFrame
        old_gdf: 旧的GeoDataFrame
        tolerance: 容差（米），默认0.1米

    Returns:
        合并后的GeoDataFrame，只包含new和old都有的记录
    """
    if new_gdf.empty or old_gdf.empty:
        return gpd.GeoDataFrame()

    # 给new中所有字段加上后缀_1避免重合（几何列除外）
    new_renamed = new_gdf.copy()
    original_geom_name = new_gdf.geometry.name
    new_columns = {}
    for col in new_gdf.columns:
        if col != original_geom_name:
            new_columns[col] = f"{col}_1"
    new_renamed = new_renamed.rename(columns=new_columns)

    # 重命名几何列，避免与old的几何列冲突
    new_geom_renamed = f"{original_geom_name}_1"
    new_buffered = new_renamed.rename_geometry(new_geom_renamed)

    # 保存old的几何列名
    old_geom_name = old_gdf.geometry.name

    # 对new几何做缓冲区，用于空间匹配
    new_buffered["_buffered_geom"] = new_buffered.geometry.buffer(tolerance)
    new_buffered = new_buffered.set_geometry("_buffered_geom")

    # 进行空间连接，保留old中与new相交的记录
    merged = gpd.sjoin(old_gdf, new_buffered, how="inner", predicate="intersects")

    # 删除sjoin产生的index_right列
    if "index_right" in merged.columns:
        merged = merged.drop(columns=["index_right"])

    # 删除临时缓冲区几何列
    if "_buffered_geom" in merged.columns:
        merged = merged.drop(columns=["_buffered_geom"])

    # 删除重复记录（一个old记录可能匹配多个new记录，保留第一个匹配）
    # 然后删除old的几何列（避免重复几何列）
    if old_geom_name in merged.columns:
        merged = merged.drop_duplicates(subset=[new_geom_renamed], keep="first")
        merged = merged.drop(columns=[old_geom_name])

    # 确保使用new的几何列作为活动几何，并恢复原始几何列名
    if new_geom_renamed in merged.columns:
        merged = merged.set_geometry(new_geom_renamed)
        merged = merged.rename_geometry(original_geom_name)

    # 重置索引
    merged = merged.reset_index(drop=True)

    return merged
