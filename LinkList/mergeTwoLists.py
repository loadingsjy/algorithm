# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 合并两个有序列表
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        p = dummy
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        return dummy.next

    def mergeTwoLists_re(self, list1, list2):
        """递归写法"""
        if list1 is None:
            return list2  # 注：如果都为空则返回空
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_re(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists_re(list1, list2.next)
        return list2

    def print_linkList(self, head):
        while head:
            print(head.val, end=", ")
            head = head.next
        print()


if __name__ == "__main__":
    lists = [[1, 4, 5], []]
    q = []
    for l in lists:
        if l:
            head = ListNode(val=l[0])
            p = head
            for val in l[1:]:
                p.next = ListNode(val)
                p = p.next
            q.append(head)
        else:
            q.append(None)

    s = Solution()
    s.print_linkList(q[0])
    s.print_linkList(q[1])

    ans = s.mergeTwoLists(q[0], q[1])
    s.print_linkList(ans)

    # ans_re = s.mergeTwoLists_re(q[0], q[1])
    # s.print_linkList(ans_re)
