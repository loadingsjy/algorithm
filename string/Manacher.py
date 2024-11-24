
# 最长回文子串，子串必须是连续的


# 最长回文子串四种解题方法：
# 1) 中心扩展法：暴力枚举，时间复杂度O(N**2)
# 2) Mananche算法：时间复杂度O(N)
# 3) 转化为求原字符串与反转字符串的最长公共子串的长度
# 4) 基于范围的动态规划


# 马拉车算法伪代码：
# def manacher(s):
#     s->处理后的字符串
#     p[]->记录每个位置的最长回文半径
#     R->记录当前所有回文串的最右边界
#     C->记录当前的最右边界的中心位置
#     L->R关于C的左侧对称点
#     n->字符串长度
#
#     for i from 0 to n-1:
#         if(i在R的外部):
#             从i开始往两边暴力扩，更新R,L,C
#         else:
#             i'为i关于C的左侧对称点
#             if(i'的回文区域彻底在L和R之间):
#                 p[i]等于i'的回文区域的长度,即p[i']
#             elif(i'的回文区域有一部分在L和R外部):
#                 p[i]等于R-i
#             else:
#                 从R之外的字符开始，往外暴力扩，然后确定p[i]，并更新L,R,C
#                 第一步扩失败了，R不变
#                 否则，R变大
#     return max(p)


def manacher(s):
    str = '#' + '#'.join(list(s)) + '#'
    n = len(str)
    p = [0] * n     # p[i]表示以i为中心的最长回文半径
    c = r = -1    # center, right
    for i in range(0, n - 1):
        if i < r:
            p[i] = min(r - i, p[2 * c - i])     # 以 i 为中心的至少回文半径
        else:
            p[i] = 1
        while i - p[i] >= 0 and i + p[i]< n:       # 暴力搜索
            if str[i + p[i]] == str[i - p[i]]:
                p[i] += 1
            else:
                break
        if i + p[i] > r:
            c, r = i, i + p[i]
    return max(p) - 1    # 去掉 '#' 的长度
    
    

if __name__ == '__main__':
    s = 'babad'
    p = manacher(s)
    print(p)
    
    s = 'cbbda'
    p = manacher(s)
    print(p)

    s = 'abcbbcba'
    p = manacher(s)
    print(p)