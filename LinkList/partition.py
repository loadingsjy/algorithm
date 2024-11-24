# 分隔链表
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 你应当 保留 两个分区中每个节点的初始相对位置。


from reverseList import print_list, ListNode, create_list_node
from copy import deepcopy


class Solution:
    def partition(self, head, x):
        dummy1 = ListNode()
        dummy2 = ListNode()

        small = dummy1
        large = dummy2
        p = head
        while p:
            if p.val < x:
                small.next = p
                small = small.next
            else:
                large.next = p
                large = large.next

            temp = p.next
            p.next = None
            p = temp

        large.next = None
        small.next = dummy2.next
        return dummy1.next


if __name__ == "__main__":
    lists = [10, 4, 8, 3, 1, 6]
    head = create_list_node(lists)
    print_list(head)
    s = Solution()

    print_list(s.partition(head, 5))
