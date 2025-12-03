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


from rule.register import *
from util import Rule


rule_list_202511 = [
    Rule(
        name="rule_1",
        description="""
当DLBM为0101/0102/0103/0201/0202/0203/0204/0301/0302/0305/0307
且DLBM_1为0201/0202/0203/0204/0301/0302/0305/0307
时
"BZ_1"不为空
        """,
        checker=check_rule_1,
    ),
    Rule(
        name="rule_2",
        description="""
当DLBM为0101/0102/0103
时
"BZ_1"≠"2024年未种植"
        """,
        checker=check_rule_2,
    ),
    Rule(
        name="rule_3",
        description="""
当DLBM_1为0101/0102/0103/0201/0202/0204/0301/0302/0305/0307/0404
时
"ZZSXDM_1"≠null
        """,
        checker=check_rule_3,
    ),
    Rule(
        name="rule_4",
        description="""
DLBM_1≠null
且DLBM_1≠""
        """,
        checker=check_rule_4,
    ),
    Rule(
        name="rule_5",
        description="""
当DLBM不为0101/0102/0103
且DLBM_1为0101/0102/0103
时
"BZ_1"不为空
        """,
        checker=check_rule_5,
    ),
    Rule(
        name="rule_6",
        description="""
当DLBM为0601
时
"BZ_1"为空
        """,
        checker=check_rule_6,
    ),
    Rule(
        name="rule_7",
        description="""
当DLBM_1为0101/0102/0103
时
BZ_1必须为"2025年未种植"
且ZZSXDM_1必须不为WG
        """,
        checker=check_rule_7,
    ),
    Rule(
        name="rule_8",
        description="""
当DLBM不为0101/0102/0103
且DLBM_1为0101/0102/0103
时
ZZSXDM_1不为WG
        """,
        checker=check_rule_8,
    ),
]

#########################################################
#########################################################
#                   旧版规则
#########################################################
#########################################################

# 旧版规则提供的筛选条件要先经过反转才能使用
rule_list_old = [
    # DLBM_1不为空
    # DLBM_1 is not null
    Rule(
        name="rule_old_1",
        description="""
DLBM_1为空
DLBM_1 is null
""",
        checker=check_rule_old_1,
    ),
    # TBXHMC_1为空，或TBXMDM_1不为空
    # TBXHMC_1 = null or TBXMDM_1 != null
    Rule(
        name="rule_old_2",
        description="""
TBXHMC_1不为空，且TBXMDM_1为空
TBXHMC_1 != null and TBXMDM_1 = null
""",
        checker=check_rule_old_2,
    ),
    # ZZSXMC_1为空，或ZZSXDM_1不为空
    # ZZSXMC_1 = null or ZZSXDM_1 != null
    Rule(
        name="rule_old_3",
        description="""
ZZSXMC_1不为空，ZZSXDM_1为空
ZZSXMC_1 != null and ZZSXDM_1 = null
""",
        checker=check_rule_old_3,
    ),
    # TBXHDM_1不属于HDGD,HQGD,LQGD,MQGD,SHGD,SMGD，或ZZSXDM_1属于LS,FLS,LYFL
    # TBXHDM_1 not in (HDGD,HQGD,LQGD,MQGD,SHGD,SMGD) or ZZSXDM_1 in (LS,FLS,LYFL)
    Rule(
        name="rule_old_4",
        description="""
TBXHDM_1属于HDGD,HQGD,LQGD,MQGD,SHGD,SMGD但是ZZSXDM_1不属于LS,FLS,LYFL
TBXHDM_1 in (HDGD,HQGD,LQGD,MQGD,SHGD,SMGD) and ZZSXDM_1 not in (LS,FLS,LYFL)
""",
        checker=check_rule_old_4,
    ),
    # XZDWKD_1小于等于8，或DLBM_1不等于1006
    # XZDWKD_1 <= 8 or DLBM_1 != 1006
    Rule(
        name="rule_old_5",
        description="""
XZDWKD_1大于8且DLBM_1=1006
XZDWKD_1 > 8 and DLBM_1 = 1006
""",
        checker=check_rule_old_5,
    ),
    # KCXS_1小于等于0，或KCDLBM_1不为空
    # KCXS_1 <= 0 or KCDLBM_1 != null
    Rule(
        name="rule_old_6",
        description="""
KCXS_1大于0且KCDLBM_1 = null
KCXS_1 > 0 and KCDLBM_1 = null
""",
        checker=check_rule_old_6,
    ),
    # KCXS_1不为0，或KCDLBM_1为空
    # KCXS_1 != 0 or KCDLBM_1 = null
    Rule(
        name="rule_old_7",
        description="""
KCXS_1为0且KCDLBM_1不为null
KCXS_1 = 0 and KCDLBM_1 != null
""",
        checker=check_rule_old_7,
    ),
    # DLBM_1为01开头，或(ZZSXDM_1为LS,FLS,LYFL,XG,LLJZ,WG且ZZSXDM_1不为空)
    # DLBM_1 like '01%' or (ZZSXDM_1 in (LS,FLS,LYFL,XG,LLJZ,WG) and ZZSXDM_1 is not null)
    Rule(
        name="rule_old_8",
        description="""
DLBM_1不为01开头，且ZZSXDM_1不为LS,FLS,LYFL,XG,LLJZ,WG，或ZZSXDM_1为null
DLBM_1 not like '01%' and (ZZSXDM_1 not in (LS,FLS,LYFL,XG,LLJZ,WG) or ZZSXDM_1 is null)
""",
        checker=check_rule_old_8,
    ),
    # DLBM_1 以 "01" 开头，或 KCXS_1 小于等于 0
    # DLBM_1 like '01%' or KCXS_1 <= 0
    Rule(
        name="rule_old_9",
        description="""
DLBM_1 不以 "01" 开头，且 KCXS_1 大于 0
DLBM_1 not like '01%' and KCXS_1 > 0
""",
        checker=check_rule_old_9,
    ),
    # DLBM_1以"01"开头，或(KCDLBM_1为空或KCXS_1为空字符串)
    # DLBM_1 like '01%' or (KCDLBM_1 is null or KCXS_1 = '')
    Rule(
        name="rule_old_10",
        description="""
DLBM_1不以"01"开头而且KCDLBM_1不为null
DLBM_1 not like '01%' and (KCDLBM_1 is not null and KCXS_1 != '')
""",
        checker=check_rule_old_10,
    ),
    # ZZSXDM_1等于GCHF，或DLBM_1以02/0301/0302/0307开头，或等于0305/0403K/0404/1104/1104K/1104A
    # ZZSXDM_1 = GCHF or (DLBM_1 like '02%' or DLBM_1 like '0301%' or DLBM_1 like '0302%' or DLBM_1 = '0305' or DLBM_1 like '0307%' or DLBM_1 = '0403K' or DLBM_1 = '0404' or DLBM_1 = '1104' or DLBM_1 = '1104K' or DLBM_1 = '1104A')
    Rule(
        name="rule_old_11",
        description="""
"ZZSXDM_1" 的值不等于 "GCHF"，并且 "DLBM_1" 的值不是以 "02"、"0301"、"0302"、"0307" 开头，也不等于 "0305"、"0403K"、"0404"、"1104"、"1104K"、"1104A"。
ZZSXDM_1 != GCHF and (DLBM_1 not like '02%' and DLBM_1 not like '0301%' and DLBM_1 not like '0302%' and DLBM_1 != '0305' and DLBM_1 not like '0307%' and DLBM_1 != '0403K' and DLBM_1 != '0404' and DLBM_1 != '1104' and DLBM_1 != '1104K' and DLBM_1 != '1104A')
""",
        checker=check_rule_old_11,
    ),
    # DLBM_1不为0301,0302,0305,0307,0404,1104,1104A，或(ZZSXDM_1为JKHF或GCHF或为空)
    # DLBM_1 not in (0301,0302,0305,0307,0404,1104,1104A) or (ZZSXDM_1 = JKHF or ZZSXDM_1 = GCHF or ZZSXDM_1 is null)
    Rule(
        name="rule_old_12",
        description="""
DLBM_1为0301,0302,0305,0307,0404,1104,1104A时，ZZSXDM_1不为JKHF，GCHF且不为null
DLBM_1 in (0301,0302,0305,0307,0404,1104,1104A) and (ZZSXDM_1 != JKHF and ZZSXDM_1 != GCHF and ZZSXDM_1 is not null)
""",
        checker=check_rule_old_12,
    ),
    # DLBM_1以01/02/0301/0302/0307/1104开头，或等于0305/0403K/0404，或ZZSXDM_1为空
    # DLBM_1 like '01%' or DLBM_1 like '02%' or DLBM_1 like '0301%' or DLBM_1 like '0302%' or DLBM_1 like '0307%' or DLBM_1 like '1104%' or DLBM_1 in ('0305','0403K','0404') or (ZZSXDM_1 is null)
    Rule(
        name="rule_old_13",
        description="""
DLBM_1字段的值不以01，02，0301，0302，0307，1104开头，且不等于0305，0403K，0404时，ZZSXDM_1字段的值不能为空
DLBM_1 not like '01%' and DLBM_1 not like '02%' and DLBM_1 not like '0301%' and DLBM_1 not like '0302%' and DLBM_1 not like '0307%' and DLBM_1 not like '1104%' and DLBM_1 not in ('0305','0403K','0404')  and (ZZSXDM_1 is not null)
""",
        checker=check_rule_old_13,
    ),
    # DLBM_1不以"01"开头，或(GDPDJB_1是1/2/3/4/5且不为空)
    # DLBM_1 not like '01%' or ( GDPDJB_1 in ('1','2','3','4','5') and GDPDJB_1 is not null )
    Rule(
        name="rule_old_14",
        description="""
DLBM_1以"01"开头且GDPDJB_1不是"1"、"2"、"3"、"4"、"5"，或者GDPDJB_1为空
DLBM_1 like '01%' and ( GDPDJB_1 not in ('1','2','3','4','5') or GDPDJB_1 is null )
""",
        checker=check_rule_old_14,
    ),
    # GDPDJB_1不为2/3/4/5，或(KCXS_1不为空且不为0)，或GDLX_1不为TT
    # GDPDJB_1 not in ('2','3','4','5') or (KCXS_1 is not null and KCXS_1 != 0) or GDLX_1 != 'TT'
    Rule(
        name="rule_old_15",
        description="""
当GDPDJB_1为2/3/4/5时，且KCXS_1为空或为0，且GDLX_1为TT
GDPDJB_1 in ('2','3','4','5') and (KCXS_1 is null or KCXS_1 = 0) and GDLX_1 = 'TT'
""",
        checker=check_rule_old_15,
    ),
    # GDLX_1不为空，或GDPDJB_1不为2/3/4/5
    # GDLX_1 is not null or GDPDJB_1 not in ('2','3','4','5')
    Rule(
        name="rule_old_16",
        description="""
当GDLX_1为空，且GDPDJB_1为2/3/4/5
GDLX_1 is null and GDPDJB_1 in ('2','3','4','5')
""",
        checker=check_rule_old_16,
    ),
    # GDPDJB_1不为1，或(KCDLBM_1不为空，且GDLX_1为空，且KCXS_1为0)
    # GDPDJB_1 != '1' or ( (KCDLBM_1 is not null) and ( GDLX_1 is null ) and KCXS_1 = 0 )
    Rule(
        name="rule_old_17",
        description="""
当GDPDJB_1为1时，且(KCDLBM_1为空，或GDLX_1不为空，或KCXS_1不为0)
GDPDJB_1 = '1' and ( (KCDLBM_1 is null) or ( GDLX_1 is not null ) or KCXS_1 != 0 )
""",
        checker=check_rule_old_17,
    ),
    # CZCSXM_1不为空，或(DLBM_1不以05/06/07/08/09开头，且不等于1004/1005/1201)
    # ( CZCSXM_1 is not null ) or (DLBM_1 not like '05%' and DLBM_1 not like '06%' and DLBM_1 not like '07%' and DLBM_1 not like '08%' and DLBM_1 not like '09%' and DLBM_1!='1004' and DLBM_1!='1005' and DLBM_1!='1201')
    Rule(
        name="rule_old_18",
        description="""
当CZCSXM_1为空，且DLBM_1以"05"、"06"、"07"、"08"、"09"开头，或等于"1004"、"1005"、"1201"
( CZCSXM_1 is null ) and (DLBM_1 like '05%' or DLBM_1 like '06%' or DLBM_1 like '07%' or DLBM_1 like '08%' or DLBM_1 like '09%' or DLBM_1='1004' or DLBM_1='1005' or DLBM_1='1201')
""",
        checker=check_rule_old_18,
    ),
    # DLBM_1不为0602/0603/1201，或CZCSXM_1为201/202/203/204/205
    # DLBM_1 not in ('0602','0603','1201') or CZCSXM_1 in ('201','202','203','204','205')
    Rule(
        name="rule_old_19",
        description="""
当DLBM_1为0602/0603/1201，且CZCSXM_1不为201/202/203/204/205
DLBM_1 in ('0602','0603','1201') and CZCSXM_1 not in ('201','202','203','204','205')
""",
        checker=check_rule_old_19,
    ),
    # DLBM_1为1001/1002/1003/1004/1006/1009/1101/1107/1107A，或(XZDWKD_1为空或为0)
    # DLBM_1 in ('1001','1002','1003','1004','1006','1009','1101','1107','1107A') or (XZDWKD_1 is null or XZDWKD_1 = 0)
    Rule(
        name="rule_old_20",
        description="""
当DLBM_1不为1001/1002/1003/1004/1006/1009/1101/1107/1107A，且XZDWKD_1不为空且不为0
DLBM_1 not in ('1001','1002','1003','1004','1006','1009','1101','1107','1107A') and (XZDWKD_1 is not null and XZDWKD_1 != 0)
""",
        checker=check_rule_old_20,
    ),
    # DLBM_1不为1001/1003/1006/1009/1107/1107A，或(XZDWKD_1不为空且不为0)
    # DLBM_1 not in ('1001','1003','1006','1009','1107','1107A') or (XZDWKD_1 is not null and XZDWKD_1 != 0)
    Rule(
        name="rule_old_21",
        description="""
当DLBM_1为1001/1003/1006/1009/1107/1107A，且XZDWKD_1为空或为0
DLBM_1 in ('1001','1003','1006','1009','1107','1107A') and (XZDWKD_1 is null or XZDWKD_1 = 0)
""",
        checker=check_rule_old_21,
    ),
    # GDLX_1等于PD，或GDPDJB_1不等于2，或KCXS_1等于0.068
    # GDLX_1 = PD or GDPDJB_1 != '2' or KCXS_1 = 0.068
    Rule(
        name="rule_old_22",
        description="""
当GDLX_1不等于PD，且GDPDJB_1等于2，且KCXS_1不等于0.068
GDLX_1 != PD and GDPDJB_1 = '2' and KCXS_1 != 0.068
""",
        checker=check_rule_old_22,
    ),
    # GDLX_1等于PD，或GDPDJB_1不等于3，或KCXS_1等于0.1195
    # GDLX_1 = PD or GDPDJB_1 != '3' or KCXS_1 = 0.1195
    Rule(
        name="rule_old_23",
        description="""
当GDLX_1不等于PD，且GDPDJB_1等于3，且KCXS_1不等于0.1195
GDLX_1 != PD and GDPDJB_1 = '3' and KCXS_1 != 0.1195
""",
        checker=check_rule_old_23,
    ),
    # GDLX_1等于PD，或GDPDJB_1不等于4，或KCXS_1等于0.1886
    # GDLX_1 = PD or GDPDJB_1 != '4' or KCXS_1 = 0.1886
    Rule(
        name="rule_old_24",
        description="""
当GDLX_1不等于PD，且GDPDJB_1等于4，且KCXS_1不等于0.1886
GDLX_1 != PD and GDPDJB_1 = '4' and KCXS_1 != 0.1886
""",
        checker=check_rule_old_24,
    ),
    # GDLX_1等于PD，或GDPDJB_1不等于5，或KCXS_1等于0.2557
    # GDLX_1 = PD or GDPDJB_1 != '5' or KCXS_1 = 0.2557
    Rule(
        name="rule_old_25",
        description="""
当GDLX_1不等于PD，且GDPDJB_1等于5，且KCXS_1不等于0.2557
GDLX_1 != PD and GDPDJB_1 = '5' and KCXS_1 != 0.2557
""",
        checker=check_rule_old_25,
    ),
    Rule(
        name="rule_old_26",
        description="""
None
""",
        checker=check_rule_old_26,
    ),
    Rule(
        name="rule_old_27",
        description="""
None
""",
        checker=check_rule_old_27,
    ),
    Rule(
        name="rule_old_28",
        description="""
None
""",
        checker=check_rule_old_28,
    ),
    # DLBM_1 不为 0310
    # DLBM_1 != '0310'
    Rule(
        name="rule_old_29",
        description="""
DLBM_1 为 0310
DLBM_1 = '0310'
""",
        checker=check_rule_old_29,
    ),
    # KCDLBM_1 不为空且不为0
    # KCDLBM_1 is not '' and KCDLBM_1 != 0
    Rule(
        name="rule_old_30",
        description="""
KCDLBM_1 为空或为0
KCDLBM_1 is '' or KCDLBM_1 = 0
""",
        checker=check_rule_old_30,
    ),
    # ZZSXDM_1 不为 GCHF 且不为空
    # ZZSXDM_1 != 'GCHF' and ZZSXDM_1 is not null
    Rule(
        name="rule_old_31",
        description="""
ZZSXDM_1 为 GCHF 或为空
ZZSXDM_1 = 'GCHF' or ZZSXDM_1 is null
""",
        checker=check_rule_old_31,
    ),
    # TBXHDM_1 不为空
    # TBXHDM_1 is not null
    Rule(
        name="rule_old_32",
        description="""
TBXHDM_1 为空
TBXHDM_1 is null
""",
        checker=check_rule_old_32,
    ),
]


rule_list = rule_list_202511 + rule_list_old
