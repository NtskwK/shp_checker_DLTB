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


from geopandas import GeoSeries

from util import is_null


def check_rule_1(d: GeoSeries):
    if (
        d.DLBM
        in [
            "0101",
            "0102",
            "0103",
            "0201",
            "0202",
            "0203",
            "0204",
            "0301",
            "0302",
            "0305",
            "0307",
        ]
    ) and (
        d.DLBM_1 in ["0201", "0202", "0203", "0204", "0301", "0302", "0305", "0307"]
    ):
        return not is_null(d.BZ_1)
    return True


def check_rule_2(d: GeoSeries):
    if d.DLBM in ["0101", "0102", "0103"]:
        return d.BZ_1 != "2024年未种植"
    return True


def check_rule_3(d: GeoSeries):
    if d.DLBM_1 in [
        "0101",
        "0102",
        "0103",
        "0201",
        "0202",
        "0204",
        "0301",
        "0302",
        "0305",
        "0307",
        "0404",
    ]:
        return not is_null(d.ZZSXDM_1)
    return True


def check_rule_4(d: GeoSeries):
    return not is_null(d.DLBM_1)


def check_rule_5(d: GeoSeries):
    if (d.DLBM not in ["0101", "0102", "0103"]) and (
        d.DLBM_1 in ["0101", "0102", "0103"]
    ):
        return not is_null(d.BZ_1)
    return True


def check_rule_6(d: GeoSeries):
    if d.DLBM == "0601":
        return is_null(d.BZ_1)
    return True


def check_rule_7(d: GeoSeries):
    if d.DLBM_1 in ["0101", "0102", "0103"]:
        if not d.BZ_1 == "2025年未种植":
            return False
        return d.ZZSXDM_1 != "WG"
    return True


def check_rule_8(d: GeoSeries):
    if (d.DLBM not in ["0101", "0102", "0103"]) and (
        d.DLBM_1 in ["0101", "0102", "0103"]
    ):
        return d.ZZSXDM_1 != "WG"
    return True


def check_rule_old_1(d: GeoSeries):
    return not is_null(d.DLBM_1)


def check_rule_old_2(d: GeoSeries):
    return is_null(d.TBXHMC_1) or not is_null(d.TBXMDM_1)


def check_rule_old_3(d: GeoSeries):
    return is_null(d.ZZSXMC_1) or not is_null(d.ZZSXDM_1)


def check_rule_old_4(d: GeoSeries):
    return d.TBXHDM_1 not in [
        "HDGD",
        "HQGD",
        "LQGD",
        "MQGD",
        "SHGD",
        "SMGD",
    ] or d.ZZSXDM_1 in ["LS", "FLS", "LYFL"]


def check_rule_old_5(d: GeoSeries):
    return is_null(d.XZDWKD_1) or d.XZDWKD_1 <= 8 or d.DLBM_1 != "1006"


def check_rule_old_6(d: GeoSeries):
    return is_null(d.KCXS_1) or d.KCXS_1 <= 0 or not is_null(d.KCDLBM_1)


def check_rule_old_7(d: GeoSeries):
    return d.KCXS_1 != 0 or is_null(d.KCDLBM_1)


def check_rule_old_8(d: GeoSeries):
    return str(d.DLBM_1).startswith("01") or (
        d.ZZSXDM_1 in ["LS", "FLS", "LYFL", "XG", "LLJZ", "WG"]
        and not is_null(d.ZZSXDM_1)
    )


def check_rule_old_9(d: GeoSeries):
    return str(d.DLBM_1).startswith("01") or is_null(d.KCXS_1) or d.KCXS_1 <= 0


def check_rule_old_10(d: GeoSeries):
    return str(d.DLBM_1).startswith("01") or (is_null(d.KCDLBM_1) or is_null(d.KCXS_1))


def check_rule_old_11(d: GeoSeries):
    return d.ZZSXDM_1 == "GCHF" or (
        str(d.DLBM_1).startswith(("02", "0301", "0302", "0307"))
        or d.DLBM_1 in ["0305", "0403K", "0404", "1104", "1104K", "1104A"]
    )


def check_rule_old_12(d: GeoSeries):
    return d.DLBM_1 not in [
        "0301",
        "0302",
        "0305",
        "0307",
        "0404",
        "1104",
        "1104A",
    ] or (d.ZZSXDM_1 == "JKHF" or d.ZZSXDM_1 == "GCHF" or is_null(d.ZZSXDM_1))


def check_rule_old_13(d: GeoSeries):
    return (
        str(d.DLBM_1).startswith(("01", "02", "0301", "0302", "0307", "1104"))
        or d.DLBM_1 in ["0305", "0403K", "0404"]
        or is_null(d.ZZSXDM_1)
    )


def check_rule_old_14(d: GeoSeries):
    return not str(d.DLBM_1).startswith("01") or (
        d.GDPDJB_1 in ["1", "2", "3", "4", "5"] and not is_null(d.GDPDJB_1)
    )


def check_rule_old_15(d: GeoSeries):
    return (
        d.GDPDJB_1 not in ["2", "3", "4", "5"]
        or (not is_null(d.KCXS_1) and d.KCXS_1 != 0)
        or d.GDLX_1 != "TT"
    )


def check_rule_old_16(d: GeoSeries):
    return not is_null(d.GDLX_1) or d.GDPDJB_1 not in ["2", "3", "4", "5"]


def check_rule_old_17(d: GeoSeries):
    return d.GDPDJB_1 != "1" or (
        (not is_null(d.KCDLBM_1)) and is_null(d.GDLX_1) and d.KCXS_1 == 0
    )


def check_rule_old_18(d: GeoSeries):
    return not is_null(d.CZCSXM_1) or (
        not str(d.DLBM_1).startswith(("05", "06", "07", "08", "09"))
        and d.DLBM_1 not in ["1004", "1005", "1201"]
    )


def check_rule_old_19(d: GeoSeries):
    return d.DLBM_1 not in ["0602", "0603", "1201"] or d.CZCSXM_1 in [
        "201",
        "202",
        "203",
        "204",
        "205",
    ]


def check_rule_old_20(d: GeoSeries):
    return d.DLBM_1 in [
        "1001",
        "1002",
        "1003",
        "1004",
        "1006",
        "1009",
        "1101",
        "1107",
        "1107A",
    ] or (is_null(d.XZDWKD_1) or d.XZDWKD_1 == 0)


def check_rule_old_21(d: GeoSeries):
    return d.DLBM_1 not in [
        "1001",
        "1003",
        "1006",
        "1009",
        "1107",
        "1107A",
    ] or (not is_null(d.XZDWKD_1) and d.XZDWKD_1 != 0)


def check_rule_old_22(d: GeoSeries):
    return d.GDLX_1 == "PD" or d.GDPDJB_1 != "2" or d.KCXS_1 == 0.068


def check_rule_old_23(d: GeoSeries):
    return d.GDLX_1 == "PD" or d.GDPDJB_1 != "3" or d.KCXS_1 == 0.1195


def check_rule_old_24(d: GeoSeries):
    return d.GDLX_1 == "PD" or d.GDPDJB_1 != "4" or d.KCXS_1 == 0.1886


def check_rule_old_25(d: GeoSeries):
    return d.GDLX_1 == "PD" or d.GDPDJB_1 != "5" or d.KCXS_1 == 0.2557


def check_rule_old_26(d: GeoSeries):
    return True


def check_rule_old_27(d: GeoSeries):
    return True


def check_rule_old_28(d: GeoSeries):
    return True


def check_rule_old_29(d: GeoSeries):
    return d.DLBM_1 != "0310"


def check_rule_old_30(d: GeoSeries):
    return not is_null(d.KCDLBM_1) and d.KCDLBM_1 != 0


def check_rule_old_31(d: GeoSeries):
    return d.ZZSXDM_1 != "GCHF" and not is_null(d.ZZSXDM_1)


def check_rule_old_32(d: GeoSeries):
    return not is_null(d.TBXHDM_1)
