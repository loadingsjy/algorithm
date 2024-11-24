# 相交链表
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
# 题目数据 保证 整个链式结构中不存在环。
# 注意，函数返回结果后，链表必须 保持其原始结构 。

from reverseList import print_list, ListNode
from copy import deepcopy
import pytest


class Solution:
    def getIntersectionNode(self, headA, headB):
        """先求出两个链表的长度，然后让长的链表先走差值步，然后两个链表同时走，直到遇到相同节点，或者走到链表尾部。"""
        n1 = 0
        n2 = 0
        if not headA or not headB:
            return None
        n1, n2 = 0, 0
        p1, p2 = headA, headB
        while p1:
            n1 += 1
            p1 = p1.next
        while p2:
            n2 += 1
            p2 = p2.next
        p1, p2 = headA, headB
        if n1 > n2:
            for _ in range(n1 - n2):
                p1 = p1.next
        else:
            for _ in range(n2 - n1):
                p2 = p2.next
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None

    def getIntersectionNode2(self, headA, headB):
        """官方答案：双指针
        当链表 headA 和 headB 都不为空时，创建两个指针 pA 和 pB，初始时分别指向两个链表的头节点 headA 和 headB，然后将两个指针依次遍历两个链表的每个节点。
        具体做法如下：
        * 每步操作需要同时更新指针 pA 和 pB。
        * 如果指针 pA 不为空，则将指针 pA 移到下一个节点；如果指针 pB 不为空，则将指针 pB 移到下一个节点。
        * 如果指针 pA 为空，则将指针 pA 移到链表 headB 的头节点；如果指针 pB 为空，则将指针 pB 移到链表 headA 的头节点。
        * 当指针 pA 和 pB 指向同一个节点或者都为空时，返回它们指向的节点或者 null。"""
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


# 创建一个辅助函数，用于生成链表
def create_list_node(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def test_getIntersectionNode_intersect():
    # 创建两个链表，假设它们在某个节点相交
    listA = create_list_node([4, 1, 8, 4, 5])
    listB = create_list_node([5, 6, 1])
    # 让两个链表在值为8的节点相交
    intersect_node = listA.next.next
    listB.next.next = intersect_node

    solution = Solution()
    intersect_result = solution.getIntersectionNode(listA, listB)

    # 验证相交节点是否正确
    assert (
        intersect_result == intersect_node
    ), "The intersecting node should be the one with value 8."


# 测试不相交链表的情况
def test_getIntersectionNode_no_intersect():
    listA = create_list_node([1, 2, 3])
    listB = create_list_node([4, 5, 6])

    solution = Solution()
    intersect_result = solution.getIntersectionNode(listA, listB)

    # 验证相交节点是否为None
    assert intersect_result is None, "There should be no intersecting node."


# 可以运行此测试用例来确认测试是否通过
if __name__ == "__main__":
    test_getIntersectionNode_intersect()
    test_getIntersectionNode_no_intersect()
    # pytest.main()
