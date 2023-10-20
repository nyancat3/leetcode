#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        # reverse
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        curr = prev if n != 1 else prev.next
        prev = None
        count = 1
        while curr:
            count += 1
            if count != n:
                next_node = curr.next
            else:
                next_node = curr.next.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
# @lc code=end
