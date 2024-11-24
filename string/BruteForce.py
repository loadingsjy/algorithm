
# 暴力字符串匹配算法
# 时间复杂度O(n*m)
# 空间复杂度O(1)
def brute_force(pattern: str, text: str) -> str:
    res = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            res.append(i)
    return res

def brute_force_v2(pattern: str, text: str) -> str:
    res = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i] != pattern[0]:
            continue
        j = 1
        while j < len(pattern) and text[i+j] == pattern[j]:
            j += 1
        if j == len(pattern):
            res.append(i)
    return res
    



if __name__ == "__main__":
    pattern = "abcab"
    text = "abababa"
    print(brute_force(pattern, text))
    print(brute_force_v2(pattern, text))
    
    pattern = "abcab"
    text = "abababcababcab"
    print(brute_force(pattern, text))
    print(brute_force_v2(pattern, text))

    pattern = "aabaaf"
    text = "aabaabaaf"
    print(brute_force(pattern, text))
    print(brute_force_v2(pattern, text))

    
    pattern = "aabaa"
    text = "aabaabaafaabaabaaf"
    print(brute_force(pattern, text))
    print(brute_force_v2(pattern, text))
    
    
    
    