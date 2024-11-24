# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 不允许修改 链表。

from reverseBetween import print_list, ListNode


class Solution:
    def detectCycle(self, head):
        """快慢指针"""
        if not head or not head.next:
            return None
        low, fast = head, head  # 不能修改fast = head.next会有bug
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if fast == low:
                p = head
                while p != low:
                    p = p.next
                    low = low.next
                return low
        return None

    def detectCycle2(self, head):
        if not head or not head.next or not head.next.next:
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        # 找到环的起始节点
        p1 = head
        p2 = slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    p = head
    for i in range(2, 10):
        node = ListNode(val=i)
        p.next = node
        p = p.next

    print_list(head)

    head.next.next.next.next.next.next.next.next = head.next.next.next.next
    print(s.detectCycle(head).val)
    print(s.detectCycle2(head).val)
