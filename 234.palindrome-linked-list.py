#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import re


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next

            # https://hibiki-press.tech/python/reference_copy/590

            # rev, rev.next, slow = slow, rev, slow.next # smarter
            temprev = rev
            rev = slow # input slow's object address (id)
            slow = slow.next # inputting value to slow changes its address (id)
            rev.next = temprev # input only rev's object address to rev.next but does not input slow's address because it has been changed
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

# @lc code=end
