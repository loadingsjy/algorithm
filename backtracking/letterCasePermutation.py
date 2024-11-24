# 字母大小写全排序：
# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
# 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。
# 示例 1：
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
# 示例 2:
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]


class Solution:
    def letterCasePermutation_bfs(self, s: str) -> list[str]:
        '''BFS'''
        s_l = list(s)
        queue = ['']

        for i, ch in enumerate(s_l):
            temp = []
            while queue:
                temp.append(queue.pop(0))
            for t in temp:
                queue.append(''.join((t, ch)))
                if ch.isalpha():
                    queue.append(''.join((t, ch.swapcase())))
        return queue
    
    
    
    def letterCasePermutation_backtrack(self, s: str) -> list[str]:
        '''回溯法'''
        ans = []
        sl = list(s)
        n = len(s)

        def dfs(i):
            if sl[i].isdigit() and i < n:
                i += 1
            if i == n:
                ans.append(''.join(sl))
                return
            
            dfs(i + 1)
            sl[i] = sl[i].swapcase()
            dfs(i + 1)
            sl[i] = sl[i].swapcase()

        dfs(0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "a1b2"
    print(sol.letterCasePermutation_bfs(s))
    print(sol.letterCasePermutation_backtrack(s))
