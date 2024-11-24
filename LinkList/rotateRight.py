# 旋转链表
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
# 示例 2：
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        if head is None:
            return head
        n = 1
        end = head
        # 找到最后一个节点，以及确定链表长度
        while end.next:
            end = end.next
            n += 1
        k %= n
        if k == 0:
            return head

        p0 = head
        for _ in range(n - k - 1):
            p0 = p0.next
        new_head = p0.next
        p0.next = None
        end.next = head
        return new_head


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

    print_list(s.rotateRight(head, 3))
