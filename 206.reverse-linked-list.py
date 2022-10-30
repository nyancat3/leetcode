#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative: Time complexity: O(n), Memory Complexity: O(1)
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

        # recursive: Time Complexity: O(n), Memory Complexity: O(n)
        # def recursive(prev, curr):
        #     if not curr:
        #         return prev
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        #     return recursive(prev, curr)
        # return recursive(None, head)
# @lc code=end
