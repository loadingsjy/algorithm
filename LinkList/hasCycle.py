# 给你一个链表的头节点 head ，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。

from reverseBetween import print_list, ListNode


class Solution:
    def hasCycle(self, head) -> bool:
        """快慢指针"""
        low, fast = head, head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if fast == low:
                return True
        return False

    def hasCycle2(self, head) -> bool:
        """哈希表"""
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    p = head
    for i in range(2, 10):
        node = ListNode(val=i)
        p.next = node
        p = p.next

    # print_list(head)

    print(s.hasCycle(head))

    head.next.next.next.next.next = head.next.next.next
    print(s.hasCycle(head))
