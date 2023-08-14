# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(10**5)   # Avoid ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

        num_list = []
        pointer = head
        while pointer:
            num_list.append(pointer.val)
            pointer = pointer.next

        num = 0
        for i in range(len(num_list)):
            num += num_list[len(num_list) - 1 - i] * pow(10, i)
        doubled_num = num * 2

        answer_head = ListNode()
        answer_tail = answer_head

        for c in str(doubled_num):
            answer_tail.next = ListNode(int(c))
            answer_tail = answer_tail.next
        return answer_head.next
