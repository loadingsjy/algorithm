# 人民币转换:
# 描述
# 考试题目和要点：
# 1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。
# 2、中文大写金额数字到“元”为止的，在“元”之后，应写“整字，如532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写”整字。
# 3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，中文大写金额中间只写一个“零”字，如6007.14，应写成“人民币陆仟零柒元壹角肆分“。
# 4、10应写作“拾”，100应写作“壹佰”。例如，1010.00应写作“人民币壹仟零拾元整”，110.00应写作“人民币壹佰拾元整”
# 5、十万以上的数字接千不用加“零”，例如，30105000.00应写作“人民币叁仟零拾万伍仟元整”

# 输入描述：
# 输入一个double数

# 输出描述：
# 输出人民币格式

# 示例1:
# 输入：151121.15
# 输出：人民币拾伍万壹仟壹佰贰拾壹元壹角伍分
# 示例2
# 输入：1010.00
# 输出：人民币壹仟零拾元整

import sys

shiwei = {
    0: "零",
    1: "壹",
    2: "贰",
    3: "叁",
    4: "肆",
    5: "伍",
    6: "陆",
    7: "柒",
    8: "捌",
    9: "玖",
    10: "拾",
}

jinwei = ["拾", "佰", "仟", "万", "亿"]


def xiaoshuToRMB(num):
    if num == 0:
        return "整"

    res = ""
    jiao = num // 10
    fen = num % 10

    if jiao != 0:
        res += shiwei[jiao] + "角"
    if fen != 0:
        res += shiwei[fen] + "分"

    return res


def _1to9(num):
    if num < 0 or num > 9:
        return ""
    return shiwei[num]


def _1to99(num, hasBai=False):
    if num < 0 or num > 99:
        return ""
    if 0 <= num < 10:
        return _1to9(num)
    shi = num // 10
    rest = num % 10
    if shi == 1 and not hasBai:
        return jinwei[0] + _1to9(rest)
    else:
        return _1to9(shi) + jinwei[0] + _1to9(rest)


def _1to999(num):
    if num < 0 or num > 999:
        return ""
    if 0 <= num <= 99:
        return _1to99(num)

    res = _1to99(num // 100) + jinwei[1]
    rest = num % 100

    if rest == 0:
        return res
    elif rest >= 10:
        res += _1to99(rest, True)
    else:
        res += "零" + _1to9(rest)
    return res


def _1to9999(num):
    if num < 0 or num > 9999:
        return ""

    if 0 <= num <= 999:
        return _1to999(num)

    res = _1to9(num // 1000) + jinwei[2]
    rest = num % 1000
    if rest == 0:
        return res
    elif rest >= 100:
        res += _1to999(rest)
    else:
        res += "零" + _1to99(rest)
    return res


def _1to99999999(num):
    if num < 0 or num > 99999999:
        return ""
    wan = num // 10000
    rest = num % 10000
    if wan == 0:
        return _1to9999(rest)
    res = _1to9999(wan) + jinwei[3]
    if rest == 0:
        return res
    else:
        if rest < 1000:
            return res + "零" + _1to999(rest)
        else:
            return res + _1to9999(rest)


def _1to999999999999(num):
    if num < 0 or num > 999999999999:
        return ""
    yi = num // 100000000
    rest = num % 100000000
    if yi == 0:
        return _1to99999999(rest)
    res = _1to9999(yi) + jinwei[4]
    if rest == 0:
        return res
    else:
        if rest < 10000000:
            return res + "零" + _1to99999999(rest)
        else:
            return res + _1to99999999(rest)


def NumstrToRMB(num_str):

    zhengshu = int(num_str.split(".")[0])
    xiaoshu = int(num_str.split(".")[1])

    zs_string = _1to999999999999(abs(zhengshu))
    xiaoshu_string = xiaoshuToRMB(xiaoshu)

    if zhengshu == 0:
        res = "人民币" + xiaoshu_string
    elif zhengshu > 0:
        res = "人民币" + zs_string + "元" + xiaoshu_string
    else:
        res = "人民币负" + zs_string + "元" + xiaoshu_string

    return res


if __name__ == "__main__":
    num_str = "512313121.15"
    print(num_str)
    print(NumstrToRMB(num_str))

    num_str = "30001.30"
    print(num_str)
    print(NumstrToRMB(num_str))

    num_str = "-300041.30"
    print(num_str)
    print(NumstrToRMB(num_str))
