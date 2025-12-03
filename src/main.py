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

from tkinter import filedialog
import sys

from tqdm import tqdm

from loader import load_gdf
from logger import logger
from geographical import geographical_comparison
from rule.list import rule_list


def main():
    ole_path = filedialog.askopenfilename(
        title="选择旧版文件",
        filetypes=[("Shapefile", "*.shp"), ("All Files", "*.*")],
    )
    if not ole_path:
        logger.error("未选择文件，程序退出")
        sys.exit(1)

    new_path = filedialog.askopenfilename(
        title="选择新版文件",
        filetypes=[("Shapefile", "*.shp"), ("All Files", "*.*")],
    )
    if not new_path:
        logger.error("未选择文件，程序退出")
        sys.exit(1)

    logger.info("开始加载旧版文件：{}", ole_path)
    old_series = load_gdf(ole_path)
    logger.info("旧版文件加载完成，记录数：{}", len(old_series))

    logger.info("开始加载新版文件：{}", new_path)
    new_series = load_gdf(new_path)
    logger.info("新版文件加载完成，记录数：{}", len(new_series))

    merged_gdf = geographical_comparison(new_series, old_series, 0)

    acc = 0
    for data in tqdm(merged_gdf.itertuples(), desc="校验数据", total=len(merged_gdf)):
        is_right = True
        for idx, rule in enumerate(rule_list):
            if not rule.checker(data):  # type: ignore
                logger.error(
                    f"更新后标识码：{data.BSM_1}， 规则编号：{idx + 1}，校验失败"
                )
                is_right = False

        acc += int(is_right)

    logger.info(f"校验通过的记录数：{acc} / {len(merged_gdf)}")
    # 打印校验规则
    for idx, rule in enumerate(rule_list):
        logger.info(f"\n规则：{rule.name}，规则描述：\n{rule.description}")

    while True:
        input("检查已结束，请打开logs文件夹查看最新的检查报告...")


if __name__ == "__main__":
    main()
