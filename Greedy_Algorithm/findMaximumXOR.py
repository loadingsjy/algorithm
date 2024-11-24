#
# * 421. 数组中两个数的最大异或值 - M
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。

# 示例 1：
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28.
# 示例 2：
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127

# 提示：
# 1 <= nums.length <= 2 * 10^5
# 0 <= nums[i] <= 2^31 - 1


class Trie:
    def __init__(self):
        # 左子树指向表示 0 的子节点
        self.left = None
        # 右子树指向表示 1 的子节点
        self.right = None


class Solution:
    cnt = 1

    def findMaximumXOR(self, nums: list[int]) -> int:
        """前缀树"""
        tree = [[0, 0] for _ in range(200001)]
        max_num = max(nums)
        high = 0
        while max_num:
            max_num >>= 1
            high += 1

        def build(nums):
            self.cnt = 1
            """构建二进制前缀树"""
            for num in nums:
                insert(num)

        def insert(num):
            """在前缀树中插入一个数num"""
            cur = 1
            for i in range(high, -1, -1):
                path = (num >> i) & 1
                if tree[cur][path] == 0:
                    self.cnt += 1
                    tree[cur][path] = self.cnt
                cur = tree[cur][path]

        def maxXor(num):
            """给定一个数，在前缀树种查找一个数，找到异或结果的最大值"""
            cur, ans = 1, 0
            for i in range(high, -1, -1):
                # status : num第i位的状态
                status = (num >> i) & 1
                # want : num第i位希望遇到的状态
                want = status ^ 1
                if tree[cur][want] == 0:  # 询问前缀树，能不能达成
                    # 不能达成
                    want ^= 1
                # want变成真的往下走的路
                ans |= (status ^ want) << i
                cur = tree[cur][want]
            return ans

        build(nums)
        ans = 0
        for num in nums:
            ans = max(ans, maxXor(num))
        return ans

    def findMaximumXOR2(self, nums: list[int]) -> int:
        # 字典树的根节点
        root = Trie()
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        def add(num: int):
            cur = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right

        def check(num: int) -> int:
            cur = root
            x = 0
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    # a_i 的第 k 个二进制位为 0，应当往表示 1 的子节点 right 走
                    if cur.right:
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
                else:
                    # a_i 的第 k 个二进制位为 1，应当往表示 0 的子节点 left 走
                    if cur.left:
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
            return x

        n = len(nums)
        x = 0
        for i in range(1, n):
            # 将 nums[i-1] 放入字典树，此时 nums[0 .. i-1] 都在字典树中
            add(nums[i - 1])
            # 将 nums[i] 看作 ai，找出最大的 x 更新答案
            x = max(x, check(nums[i]))

        return x

    def findMaximumXOR(self, nums: list[int]) -> int:
        """宫水三叶"""
        N, idx = (len(nums) + 1) * 31, 0
        tr = [[0, 0] for _ in range(N)]

        def add(x):
            nonlocal idx
            p = 0
            for i in range(31, -1, -1):
                u = (x >> i) & 1
                if tr[p][u] == 0:
                    idx += 1
                    tr[p][u] = idx
                p = tr[p][u]

        def getVal(x):
            p, ans = 0, 0
            for i in range(31, -1, -1):
                a = (x >> i) & 1
                b = 1 - a
                if tr[p][b] != 0:
                    ans |= b << i
                    p = tr[p][b]
                else:
                    ans |= a << i
                    p = tr[p][a]
            return ans

        ans = 0
        for i in nums:
            add(i)
            j = getVal(i)
            ans = max(ans, i ^ j)
        return ans

    def findMaximumXOR3(self, nums: list[int]) -> int:
        # 最高位的二进制位编号为 30
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            # 将所有的 pre^k(a_j) 放入哈希表中
            for num in nums:
                # 如果只想保留从最高位开始到第 k 个二进制位为止的部分
                # 只需将其右移 k 位
                seen.add(num >> k)

            # 目前 x 包含从最高位开始到第 k+1 个二进制位为止的部分
            # 我们将 x 的第 k 个二进制位置为 1，即为 x = x*2+1
            x_next = x * 2 + 1
            found = False

            # 枚举 i
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found:
                x = x_next
            else:
                # 如果没有找到满足等式的 a_i 和 a_j，那么 x 的第 k 个二进制位只能为 0
                # 即为 x = x*2
                x = x_next - 1

        return x

    def findMaximumXOR4(self, nums: list[int]) -> int:
        """哈希表 + 贪心: 从最高位开始，每次贪心的选择能使当前位异或和为1的两个数，如果不能，该位只能是0
        1.初始化答案 ans=0。

        2.从最高位开始枚举 i，也就是 max(nums) 的二进制长度减一。

        3.设 newAns=ans+2^i ，看能否从 nums 中选两个数（低于 i 的比特位当作 0），满足这两个数的异或和等于 newAns。
        如果可以，则更新 ans 为 newAns，否则 ans 保持不变。

        4.判断【两数异或】的做法和力扣第一题【两数之和】是一样的，请看 我的题解。用 ⊕ 表示异或，
        如果 a⊕b=newAns，那么两边同时异或 b，由于 b⊕b=0，所以得到 a=newAns⊕b（相当于把两数之和代码中的减法改成异或）。
        这样就可以一边枚举 b，一边在哈希表中查找 newAns⊕b 了。
        """
        max_num = max(nums)
        high = 0
        while max_num:
            max_num >>= 1
            high += 1

        ans = 0  # ans : 31....i+1位 已经达成的目标
        seen = set()
        for i in range(high, -1, -1):  # 从最高位开始枚举
            better = ans | (1 << i)  # 问第i为上能不能设置成1
            seen.clear()
            for num in nums:
                # num : 31.....i 这些状态保留，剩下全成0
                num = (num >> i) << i
                seen.add(num)
                # num 异或上 某状态 是否能 达成better目标，就在set中找 某状态 : better ^ num
                if better ^ num in seen:
                    ans = better
                    break
        return ans

    def findMaximumXOR5(self, nums: list[int]) -> int:
        """灵神写法"""
        ans = mask = 0
        high_bit = max(nums).bit_length() - 1
        for i in range(high_bit, -1, -1):  # 从最高位开始枚举
            mask |= 1 << i
            new_ans = ans | (1 << i)  # 这个比特位可以是 1 吗？
            seen = set()
            for x in nums:
                x &= mask  # 低于 i 的比特位置为 0
                if new_ans ^ x in seen:
                    ans = new_ans  # 这个比特位可以是 1
                    break
                seen.add(x)
        return ans
