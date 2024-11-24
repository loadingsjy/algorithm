from copy import deepcopy
from typing import Optional
from reverseList import print_list, ListNode, create_list_node


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        node1, node2, temp = head, head.next, head.next
        while node2 and node2.next:
            node1.next = node2.next
            node2.next = node1.next.next
            node1 = node1.next
            node2 = node2.next
        node1.next = temp
        return head

    def oddEvenList2(self, head: ListNode) -> ListNode:
        if not head:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head


if __name__ == "__main__":
    sol = Solution()
    lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = create_list_node(lists)
    print_list(head)

    print_list(sol.oddEvenList(deepcopy(head)))
    print_list(sol.oddEvenList2(deepcopy(head)))
