# KMP算法描述：
# KMP算法是一种字符串匹配算法，它利用前缀函数来寻找模式串在文本串中的位置。
# 前缀函数是一个整数数组，其中第i个元素表示模式串的前i个字符中，最长的、同时也是模式串的前缀的后缀的长度。
# 前缀函数的计算方法是：
# 如果pattern[i] == pattern[j]，则lps[i] = j+1
# 如果pattern[i] != pattern[j]，且j!= 0，则j = lps[j-1]
# 如果pattern[i] != pattern[j]，且j == 0，则lps[i] = 0
# 前缀函数的作用是，当模式串的前缀与模式串的某一后缀相同时，可以利用前缀函数来快速定位模式串的位置。
# 算法的基本思路是，初始化j=0，i=1。然后，比较pattern[j]和text[i]。如果两者相等，则j++,i++。如果两者不等，则判断j是否为0。如果j不为0，则令j=lps[j-1]，继续比较。如果j为0，则令i++，继续比较。
# 如果j到达模式串的末尾，则说明模式串在text中出现了，将模式串的起始位置加入结果列表，并令j=lps[j-1]。
# 如果i到达text的末尾，则说明模式串不在text中出现，返回结果列表。
# 算法的时间复杂度为O(n+m)，空间复杂度为O(m)。


def kmp(pattern, text):
    m = len(pattern)
    n = len(text)
    lps = [0] * m  # 最长前后缀匹配长度数组
    j = 0  # pattern串的当前位置
    i = 1  # text串的当前位置
    # 构建lsp数组
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    # print(lps)
    i = j = 0
    result = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            result.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


def kmp_v2(pattern, text):
    """返回pattern在text中所有出现的位置，如果pattern不在text中，返回[]"""

    # pattern的长度不能大于text的长度
    if not pattern or not text or len(pattern) > len(text) or len(pattern) == 0:
        return []

    str1 = list(text)
    str2 = list(pattern)
    i1, i2 = 0, 0
    result = []
    # next[i] 数组表示模式串第i个字符的最长前后缀匹配长度（不包含第i个字符本身）
    next = get_next(str2)  # 时间复杂度 O(M)
    # 时间复杂度 O(N)
    while i1 < len(str1) and i2 < len(str2):
        if str1[i1] == str2[i2]:  # 如果字符相同，继续匹配
            i1 += 1
            i2 += 1
        if i2 == len(str2):  # 匹配成功
            result.append(i1 - i2)
            i2 = next[i2 - 1] + 1  # 继续匹配
        elif i1 < len(str1) and str1[i1] != str2[i2]:  # 匹配失败
            if next[i2] == -1:  # 如果next[i2]=-1，说明模式串的当前字符在text中不存在，需要继续匹配 可用if i2 == 0:代替
                i1 += 1
            else:  # 如果next[i2]!=-1，说明模式串的当前字符在text中存在，需要跳过next[i2]个字符
                i2 = next[i2]

    if i2 == len(str2):  # 最后匹配成功
        result.append(i1 - i2)
    return result


def get_next(pattern): 
    """返回模式串的next数组，next[i]表示模式串第i个字符的最长前后缀匹配长度（不包含第i个字符本身）"""
    m = len(pattern)
    if m == 1:
        return [-1]
    next = [0] * m
    next[0] = -1
    i = 2  # 后缀的末尾位置（不包含）
    cn = 0  # 前缀匹配的开始位置的最大长度（包含）

    # 动态规划计算next数组
    while i < m:
        if pattern[i-1] == pattern[cn]:  # 如果字符相同，则next[i] = next[i-1] + 1 = cn + 1
            next[i] = cn + 1
            cn += 1
            i += 1
        elif cn != 0:  # 如果字符不同，继续用next[cn-1]位置来匹配
            cn = next[cn - 1]
        else:  # 如果cn=0，说明最长相等前后缀的长度为0，next[i]设为0
            next[i] = 0
            i += 1
    # print(next)
    return next


if __name__ == "__main__":
    
    pattern = "abcab"
    text = "abababa"
    print(kmp(pattern, text))
    print(kmp_v2(pattern, text))
    
    pattern = "abcab"
    text = "abababcababcab"
    print(kmp(pattern, text))
    print(kmp_v2(pattern, text))

    pattern = "aabaaf"
    text = "aabaabaaf"
    print(kmp(pattern, text))
    print(kmp_v2(pattern, text))
    
    pattern = "aabaa"
    text = "aabaabaafaabaabaaf"
    print(kmp(pattern, text))
    print(kmp_v2(pattern, text))
