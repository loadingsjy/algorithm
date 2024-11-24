# 147. 对链表进行插入排序:
# 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。
# 插入排序 算法的步骤:
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。
# 每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。


from reverseList import print_list, ListNode, create_list_node
from copy import deepcopy


class Solution:
    def insertionSortList(self, head):
        """使用额外数据空间"""
        dummy = ListNode()
        p = head
        while p:
            loc = dummy
            while loc.next and loc.next.val <= p.val:
                loc = loc.next

            next_p = p.next  # 保存下一个节点
            # p.next = None
            p.next = loc.next
            loc.next = p

            p = next_p
        return dummy.next

    def insertionSortList2(self, head):
        if not head:
            return head
        """原地操作"""
        dummy = ListNode(next=head)
        cur = head.next
        # prev = dummy
        lastSorted = head
        while cur:
            if lastSorted.val <= cur.val:
                lastSorted = lastSorted.next
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                lastSorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastSorted.next

        return dummy.next


if __name__ == "__main__":
    lists = [1, 4, 2, 3, 0, 6]
    head = create_list_node(lists)
    print_list(head)
    s = Solution()

    print_list(s.insertionSortList(deepcopy(head)))
    print_list(s.insertionSortList2(deepcopy(head)))
