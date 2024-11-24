# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(next=head)
        frist = dummy
        for _ in range(n):
            if frist:
                frist = frist.next
            else:
                return head

        second = dummy
        while frist.next:
            frist = frist.next
            second = second.next
        temp = second.next
        second.next = second.next.next
        del temp
        return dummy.next


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.val, end=",  ")
        cur = cur.next
    print()


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print_list(head)

    print_list(s.removeNthFromEnd(head, 3))
