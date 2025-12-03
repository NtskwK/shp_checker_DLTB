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


from typing import Callable

from geopandas import GeoSeries
import pandas as pd


_NULL_STRINGS = frozenset({"NULL", "NAN", "NONE", "UNKNOWN", "N/A", "ND"})


def is_null(value) -> bool:
    if value is None or pd.isna(value):
        return True
    if isinstance(value, str):
        stripped = value.strip()
        return stripped == "" or stripped.upper() in _NULL_STRINGS
    return False


class Rule:
    def __init__(
        self,
        name: str,
        description: str,
        checker: Callable[[GeoSeries], bool],
    ):
        self.name = name
        self.description = description
        self.checker = checker
