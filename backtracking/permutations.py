# 打印字符串的全排列


def permute(s):
    def backtrack(first):
        if first == n:
            res.append("".join(nums))
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    n = len(s)
    nums = list(s)
    res = []
    backtrack(0)
    return list(set(res))       # 去重


def process(s, i, res):
    if i == len(s):
        res.append("".join(s))
        return
    visited = [0] * 26
    for j in range(i, len(s)):
        if visited[ord(s[j]) - ord("a")] == 0:      # 字符是否已经使用过，分支限界/剪枝
            visited[ord(s[j]) - ord("a")] = 1
            s[i], s[j] = s[j], s[i]
            process(s, i + 1, res)
            s[i], s[j] = s[j], s[i]


def permute_2(s):
    res = []
    process(list(s), 0, res)
    return res


# Test the function with some inputs:
if __name__ == "__main__":
    s = 'abca'
    s.lower()
    
    print(permute(s))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    
    print(permute_2(s))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
