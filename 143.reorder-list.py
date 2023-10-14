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
        while second and second.next:   # second.next is necessary to avoid infinite loop
            fist_next = first.next
            second_next = second.next
            first.next = second
            # print('test1', first)
            first.next.next = fist_next
            # print('test2', first)

            first = fist_next
            second = second_next

# @lc code=end
