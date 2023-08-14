# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:
            head = ListNode(0, head)
        node = head
        while node:
            node.val = node.val * 2 % 10
            if node.next and node.next.val >= 5:    # if the value is greater than or equal to 5, carry 1
                node.val += 1
            node = node.next
        return head
