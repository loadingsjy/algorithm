# Definition for singly-linked list.
from copy import deepcopy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    cur = head
    while cur is not None:
        if cur.next:
            print(cur.val, end="-->")
        else:
            print(cur.val, end="")
        cur = cur.next
    print()


# 创建一个辅助函数，用于生成链表
def create_list_node(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def reverseList(head):
    prev_node = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev_node
        prev_node = cur
        cur = next_node

    head = prev_node

    return head


def reverseList_re(head):
    if head is None or head.next is None:
        return head
    cur = reverseList_re(head.next)  # 从后往前反转
    head.next.next = head
    head.next = None
    return cur


if __name__ == "__main__":
    head = create_list_node([1, 2, 3, 4, 5, 6])
    print_list(head)
    print_list(reverseList(deepcopy(head)))
    print_list(reverseList_re(deepcopy(head)))
