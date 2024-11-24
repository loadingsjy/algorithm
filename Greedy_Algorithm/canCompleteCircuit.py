# 134. 加油站
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

# 示例 1:
# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
# 示例 2:
# 输入: gas = [2,3,4], cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """贪心算法：一句话概括：如果x到达不了y+1，那么x到y之间的点也不可能到达y+1，
        因为中间任何一点的油都是拥有前面的余量的，所以下次遍历直接从y+1开始"""
        # rest = [g - c for g, c in zip(gas, cost)]

        n = len(gas)
        i = 0
        while i < n:
            sumOfGas, sumOfCost, cnt = 0, 0, 0
            while cnt < n:
                j = (i + cnt) % n
                sumOfGas += gas[j]
                sumOfCost += cost[j]
                if sumOfCost > sumOfGas:
                    break
                cnt += 1
            if cnt == n:  # 走完一圈了
                return i
            else:  # 没有走完的话，从j的下一个节点开始走
                i = i + cnt + 1
        return -1

    def canCompleteCircuit2(self, gas: list[int], cost: list[int]) -> int:
        """滑动窗口：保证窗口内的剩余油量 >= 0
        加油站那题，力扣的解法太卷了，我研究了一下，发现在左神的解法基础上，确实可以再进行两次优化：
        1. 左边界的更新：如果发现【left, right】范围内的sum<0，即油不够的情况，左边界可以直接更新成right+1，sum和len置0。

        因为对于任意的 left < i < right，一定满足 【left, i】 范围内的sum ≥ 0(不然右边界不可能扩过来)，
        那也就意味着，从(left, right]范围内的任意位置出发，到right位置的sum都小于0，左边界left可以直接更新成right+1，而不用一点点更新left、len和sum。

        2. 右边界的更新：右边界实际不用走一圈多，右边界走到最后一个加油站的位置即可。

        根据题意，只有两种可能：要么不存在合法的加油站，要么存在唯一的加油站：
        ①是否存在合法的加油站：只需要右边界从左到右移动的时候，计算一个净油量数组的整体的累加和，判断它是否大于等于零，如果是，一定存在合法的加油站，且唯一，如果否，返回-1。
        ②既然存在合法的加油站，而你的右边界又来到了数组中的最后一个加油站，此时右边界不用再重新回到开头的地方来跑第二圈，
        因为根据①，右边界来到第一圈最后一个加油站时，就已经知道了是否存在满足题意的加油站了，
        如果净油量数组总和大于零，left就是满足题意的左边界，不可能出现“right在第二圈跑着跑着，发现left不满足题意，
        而(left,end]中又有一个满足题意的加油站”的情况，这一点可以通过第1点优化得出的结论证明。
        """
        n = len(gas)
        left, right = 0, 0
        cnt = 0  # 当前窗口的长度
        sumOfRest = 0  # 当前剩余油量
        while left < n:
            while sumOfRest >= 0:
                # 油量大于等于0就可以继续往前走
                if cnt == n:
                    return left
                right = (left + cnt) % n
                cnt += 1
                sumOfRest += gas[right] - cost[right]
            # # sumOfRest < 0
            # cnt -= 1
            # sumOfRest -= gas[left] - cost[left]
            # left += 1
            cnt = 0
            sumOfRest = 0
            if right < left:  # 说明right多跑了一圈了
                break
            left = right + 1
        return -1

    def canCompleteCircuit3(self, gas: list[int], cost: list[int]) -> int:
        """
        亏空最严重的一个点必须放在最后一步走，等着前面剩余的救助
        https://leetcode.cn/problems/gas-station/solutions/54278/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/
        """
        n = len(gas)
        spare = 0
        minSpare = float("inf")
        minIndex = 0

        for i in range(n):
            spare += gas[i] - cost[i]
            if spare <= minSpare:
                minSpare = spare
                minIndex = i

        return -1 if spare < 0 else (minIndex + 1) % n


if __name__ == "__main__":
    s = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(s.canCompleteCircuit(gas, cost))
    print(s.canCompleteCircuit2(gas, cost))
    print(s.canCompleteCircuit3(gas, cost))
