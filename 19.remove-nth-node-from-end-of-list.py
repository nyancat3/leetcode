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
        dummy_node = ListNode(None, head)
        slow, fast = dummy_node, head

        for i in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_node.next
# @lc code=end
