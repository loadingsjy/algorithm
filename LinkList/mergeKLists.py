# 合并k个升序链表
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 示例：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6


import heapq
from copy import deepcopy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists):
        """使用优先队列(堆)合并"""
        dummy = ListNode()
        p = dummy
        heap = list(filter(lambda x: x is not None, [head for head in lists]))

        heapq.heapify(heap)

        while len(heap) > 0:
            node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap, node.next)
        return dummy.next

    def print_linkList(self, head):
        while head:
            print(head.val, end=", ")
            head = head.next
        print()

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        p = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        return dummy.next

    def mergeKLists_OneByOne(self, lists):
        """逐一合并两个链表，时间复杂度：O(k^2*n)，空间复杂度O(1)"""
        ans = None
        for list_n in lists:
            ans = self.mergeTwoLists(ans, list_n)
        return ans

    def mergeKLists_bi(self, lists):
        """两两合并两个链表，时间复杂度：O(kn×logk)"""
        ans = None
        temp = lists
        while len(temp) > 1:
            if len(temp) % 2 == 1:
                t = [temp.pop()]
            else:
                t = []
            for i in range(0, len(temp) - 1, 2):
                t.append(self.mergeTwoLists(temp[i], temp[i + 1]))
            temp = t
        if temp:
            return self.mergeTwoLists(ans, temp[0])
        else:
            return ans

    def mergeKLists_bi_re(self, lists):
        """分治合并，两两合并两个链表，递归实现，时间复杂度：O(kn×logk)，空间复杂度O(logk)"""

        def dfs(lists, l, r):
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = (l + r) >> 1
            return self.mergeTwoLists(dfs(lists, l, mid), dfs(lists, mid + 1, r))

        return dfs(lists, 0, len(lists) - 1)


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6], []]
    q = []
    for l in lists:
        if l:
            head = ListNode(val=l[0])
            p = head
            for val in l[1:]:
                p.next = ListNode(val)
                p = p.next
            q.append(head)
        else:
            q.append(None)

    s = Solution()

    q_1 = deepcopy(q)
    s.print_linkList(s.mergeKLists(q_1))

    q_2 = deepcopy(q)
    s.print_linkList(s.mergeKLists_OneByOne(q_2))

    q_3 = deepcopy(q)
    s.print_linkList(s.mergeKLists_bi(q_3))

    q_4 = deepcopy(q)
    s.print_linkList(s.mergeKLists_bi_re(q_4))
