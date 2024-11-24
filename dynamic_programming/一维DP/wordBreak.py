# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        # 定义 dp 数组，dp[i] 表示 s 的前 i 个字符能否被拆分成字典中的单词
        dp = [False] * (len(s) + 1)
        dp[0] = True  # 空字符串可以被拆分

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:  # 0-j 和 j-i 都可以被拆分
                    dp[i] = True
                    break

        return dp[-1]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))  # True
