# 两数相加

# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

from reverseList import print_list, ListNode, create_list_node
from copy import deepcopy


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        p = dummy

        p1 = l1
        p2 = l2
        carry = 0
        while p1 or p2:
            num = carry
            if p1:
                num += p1.val
                p1 = p1.next
            if p2:
                num += p2.val
                p2 = p2.next
            carry = num // 10
            num %= 10
            p.next = ListNode(val=num)
            p = p.next
        if carry != 0:
            p.next = ListNode(val=carry)
        return dummy.next


if __name__ == "__main__":
    lists1 = [8, 2, 4, 1, 4, 6]
    head1 = create_list_node(lists1)
    print_list(head1)
    lists2 = [5, 1, 5, 2, 9, 6]
    head2 = create_list_node(lists2)
    s = Solution()

    print_list(s.addTwoNumbers(head1, head2))
