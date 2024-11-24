# 移除链表元素
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
from reverseList import print_list, ListNode, create_list_node
from copy import deepcopy


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(next=head)
        p = dummy

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next

    def removeElements_re(self, head, val):
        if head is None:
            return head
        head.next = self.removeElements_re(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head


if __name__ == "__main__":
    lists = [1, 2, 1, 3, 2, 1, 1]
    head = create_list_node(lists)
    print_list(head)
    s = Solution()

    print_list(s.removeElements(deepcopy(head), 1))
    print_list(s.removeElements_re(deepcopy(head), 1))
