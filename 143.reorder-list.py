#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # e.g. 1->2->3->4->5

        # find the middle: slow = 3, fast = 5
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half: 5->4->3
        prev, second = None, slow
        # slow.next = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # merge: 1->5->2->4->3
        first, second = head, prev
        while second and second.next:   # loop twice: second.next is necessary to avoid 1->5->2->4->3->3
            fist_next = first.next  # 2, 3
            second_next = second.next   # 4, 3
            first.next = second # 1->5, 2->4
            first.next.next = fist_next # 5->2, 4->3
            # 1->5->2, 1->5->2->4->3

            first = fist_next   # 2, 3
            second = second_next    # 4, 3

# @lc code=end
