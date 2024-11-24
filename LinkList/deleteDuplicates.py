# 删除排序列表中的重复元素

# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
from reverseBetween import print_list, ListNode
from copy import deepcopy


class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        p1 = head
        p2 = head.next
        while p1.next:
            if p1.val == p2.val:
                nxt = p2.next
                p1.next = nxt
                p2 = nxt
            else:
                p1 = p1.next
                p2 = p2.next
        return head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        """官方答案"""
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=2)
    p = head
    for i in range(4):
        node = ListNode(val=2)
        p.next = node
        p = p.next
    for i in range(3):
        node = ListNode(val=3)
        p.next = node
        p = p.next
    for i in range(5):
        node = ListNode(val=4)
        p.next = node
        p = p.next
    for i in range(1):
        node = ListNode(val=6)
        p.next = node
        p = p.next

    print_list(head)

    print_list(s.deleteDuplicates(deepcopy(head)))
    print_list(s.deleteDuplicates2(deepcopy(head)))
