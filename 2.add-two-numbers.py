#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_head = ListNode()
        answer_tail = answer_head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            num = val1 + val2 + carry
            carry, val = divmod(num, 10)
            answer_tail.next = ListNode(val)
            answer_tail = answer_tail.next
            # carry = (int)(num >= 10) # OK. Covert True/False into int (1/0)
            # carry = num // 10 # OK.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return answer_head.next
# @lc code=end
