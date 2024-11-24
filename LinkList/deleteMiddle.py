#
# * 2095. 删除链表的中间节点 - M
# 给你一个链表的头节点 head 。删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。
# 长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），其中 ⌊x⌋ 表示小于或等于 x 的最大整数。
# 对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。


from typing import Optional
from reverseBetween import print_list, ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(val=1)
    p = head
    for i in range(2, 8):
        node = ListNode(val=i)
        p.next = node
        p = p.next

    print_list(head)

    print_list(sol.deleteMiddle(head))
