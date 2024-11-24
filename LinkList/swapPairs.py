# 两两交换链表中的节点
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

from copy import deepcopy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        # if not head or not head.next:
        #     return head
        dummy = ListNode(next=head)
        prev = dummy
        while prev.next and prev.next.next:
            node1 = prev.next
            node2 = prev.next.next

            prev.next = node2
            # 下面两行不能交换顺序
            node1.next = node2.next
            node2.next = node1

            prev = node1
        return dummy.next

    def swapPairs_re(self, head: ListNode) -> ListNode:
        """递归法：宗旨就是紧紧抓住原来的函数究竟返回的是什么？作用是什么即可其余的细枝末节不要细究，编译器会帮我们自动完成"""

        # * base case
        if not head or not head.next:
            return head

        # * swapPairs(ListNode head) 的意义就是两两翻转链表中的节点 + 返回翻转后的新的头结点
        # * 我们知道翻转后新的头结点必然是第二个节点
        # * 举例子:1->2->3->4 翻转后:2->1->4->3
        newHead = head.next

        # * 此时tmpHead为:4->3
        tmpHead = self.swapPairs(newHead.next)

        # * 而前面的还粘连着:1->2->(3)  4->3
        # * 此时再让1->4 此时链表为:2->(3) 1->4->3
        head.next = tmpHead

        # * 再将2指向1即可 此时链表为:2->1->4->3 已经完成翻转
        newHead.next = head

        # * 返回新的头结点
        return newHead

    def swapPairs_re2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        one = head
        two = one.next
        three = two.next

        two.next = one
        one.next = self.swapPairs_re2(three)

        return two


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.val, end=",  ")
        cur = cur.next
    print()


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print_list(head)
    print()
    s = Solution()
    print_list(s.swapPairs(deepcopy(head)))

    print_list(s.swapPairs_re(deepcopy(head)))

    print_list(s.swapPairs_re2(deepcopy(head)))
