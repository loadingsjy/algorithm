# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
# 你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
# 示例 1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 示例 2：
# 输入：head = [5], left = 1, right = 1
# 输出：[5]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(next=head)
        p0 = dummy
        # 找到left节点的前一个
        for _ in range(left - 1):
            p0 = p0.next

        prev = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # 下面两句不能交换顺序
        p0.next.next = cur
        p0.next = prev

        return dummy.next


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.val, end=",  ")
        cur = cur.next
    print()


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    p = head
    for i in range(2, 10):
        node = ListNode(val=i)
        p.next = node
        p = p.next

    print_list(head)

    print_list(s.reverseBetween(head, 2, 7))
