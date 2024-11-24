# K个一组翻转链表
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev, head

    def reverseKGroup(self, head, k: int):

        dummy = ListNode(next=head)

        last_prev = dummy
        p_head = head  # 当前组的头节点
        p_tail = p_head  # 当前组的尾节点

        while p_head:
            i = 0
            while i < k - 1 and p_tail:
                p_tail = p_tail.next
                i += 1
            if p_tail is None:  # 不足k个
                break
            else:
                next_head = p_tail.next  # 保存下一组的头节点
                p_tail.next = None

            r_head, r_tail = self.reverseList(p_head)
            # print_list(r_head)
            last_prev.next = r_head  # 上一组的尾节点连到这一组的头节点
            last_prev = r_tail  # 更新上一组尾节点

            p_head = next_head
            p_tail = p_head

        if p_tail is None:
            last_prev.next = p_head

        return dummy.next

    def reverseKGroup2(self, head, k):
        """作者：灵茶山艾府"""
        # 统计节点个数
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        p0 = dummy = ListNode(next=head)
        pre = None
        cur = head

        # k 个一组处理
        while n >= k:
            n -= k
            for _ in range(k):  # 同 92 题
                nxt = cur.next
                cur.next = pre  # 每次循环只修改一个 next，方便大家理解
                pre = cur
                cur = nxt

            # 见视频
            nxt = p0.next  # 保存下一组的前面那个节点
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.val, end=",  ")
        cur = cur.next
    print()


if __name__ == "__main__":
    s = Solution()
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)
    # head.next.next.next.next.next.next = ListNode(7)
    # head.next.next.next.next.next.next.next = ListNode(8)
    head = ListNode(val=1)
    p = head
    for i in range(2, 9):
        node = ListNode(val=i)
        p.next = node
        p = p.next

    print_list(head)

    print_list(s.reverseKGroup(head, 3))
