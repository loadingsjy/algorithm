# 链表的中间节点
# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。

from reverseList import print_list, ListNode
from copy import deepcopy


class Solution:
    def middleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    p = head
    for i in range(2, 10):
        node = ListNode(val=i)
        p.next = node
        p = p.next

    print_list(head)

    print_list(s.middleNode(head))
