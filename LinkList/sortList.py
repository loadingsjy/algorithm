# 排序列表
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

from reverseList import print_list, ListNode, create_list_node
from copy import deepcopy


class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            p, p1, p2 = dummyHead, head1, head2
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
            return dummyHead.next

        return sortFunc(head, None)


if __name__ == "__main__":
    lists = [10, 4, 8, 3, 1, 6]
    head = create_list_node(lists)
    print_list(head)
    s = Solution()

    print_list(s.sortList(head))
