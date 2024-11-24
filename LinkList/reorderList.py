# 重排列表
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
from reverseList import print_list, ListNode
from copy import deepcopy


# 创建一个辅助函数，用于生成链表
def create_list_node(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def middleNode(self, head):
        low, fast = head, head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        return low

    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        # print_list(head)
        # print_list(head2)
        while head2.next:
            next1 = head.next
            next2 = head2.next

            head.next = head2
            head2.next = next1

            head = next1
            head2 = next2


if __name__ == "__main__":
    lists = [1, 2, 3, 4, 5]
    head = create_list_node(lists)
    print_list(head)
    s = Solution()

    s.reorderList(head)
    print_list(head)
