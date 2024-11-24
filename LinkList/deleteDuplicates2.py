# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

from reverseList import print_list, ListNode
from copy import deepcopy


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        dummy = ListNode(next=head)
        prev = dummy
        cur = head

        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if cur != prev.next:  # 有重复元素
                prev.next = cur.next
                cur = cur.next
            else:  # 无重复元素
                prev = prev.next
                cur = cur.next
        return dummy.next

    def deleteDuplicates2(self, head):
        """官方答案"""
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    p = head
    for i in range(4):
        p.next = ListNode(val=2)
        p = p.next

    p.next = ListNode(val=3)
    p = p.next

    for i in range(3):
        p.next = ListNode(val=4)
        p = p.next

    p.next = ListNode(val=5)
    p = p.next

    for i in range(5):
        p.next = ListNode(val=6)
        p = p.next

    for i in range(1):
        p.next = ListNode(val=7)
        p = p.next

    p.next = ListNode(val=8)
    print("orignal link list:", end="")
    print_list(head)

    print_list(s.deleteDuplicates(deepcopy(head)))
    print_list(s.deleteDuplicates2(deepcopy(head)))
