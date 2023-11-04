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

        # Solve 2 again on my own
        ans_head = ListNode()
        ans = ans_head
        carry = 0
        while l1 and l2:
            div, mod = divmod(l1.val + l2.val + carry, 10)
            ans.val = mod
            carry = div

            if l1.next and not l2.next:
                l2.next = ListNode()
            elif not l1.next and l2.next:
                l1.next = ListNode()

            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                ans.next = ListNode()
                ans = ans.next

        if carry > 0:
            ans.next = ListNode(carry)

        return ans_head

# @lc code=end
