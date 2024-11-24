# 回文链表
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

from reverseList import print_list, ListNode, create_list_node


class Solution:
    def isPalindrome(self, head):
        """复制链表值到数组列表中，使用双指针法判断是否为回文。时间复杂度O(n)，空间复杂度O(n)"""
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

    def isPalindrome_re(self, head):
        """递归，时间复杂度O(n)，空间复杂度O(n)"""
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def middleNode(self, head):
        """上中位数"""
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome_fl(self, head):
        """
        找到前半部分链表的尾节点。反转后半部分链表。判断是否回文。恢复链表。返回结果。
        1.找到前半部分链表的尾节点。
        2.反转后半部分链表。
        3.判断是否回文。
        4.恢复链表。
        5.返回结果。
        """
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        mid = self.middleNode(head)
        second_half_start = self.reverseList(mid.next)

        # 判断是否回文
        result = True
        frist = head
        second = second_half_start
        while result and second is not None:
            if frist.val != second.val:
                result = False
            frist = frist.next
            second = second.next

        # 还原链表并返回结果
        mid.next = self.reverseList(second_half_start)
        return result


if __name__ == "__main__":
    lists = [1, 2, 3, 2, 1]
    head = create_list_node(lists)
    print_list(head)
    s = Solution()

    print(s.isPalindrome(head))
    print(s.isPalindrome_re(head))
    print(s.isPalindrome_fl(head))
    print()

    lists = [1, 2]
    head = create_list_node(lists)
    print_list(head)
    s = Solution()

    print(s.isPalindrome(head))
    print(s.isPalindrome_re(head))
    print(s.isPalindrome_fl(head))
