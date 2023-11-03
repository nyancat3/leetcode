#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        curr = head
        first_node = Node(head.val)
        ans = first_node
        node_addresses = {} # {original_node: copied_node}
        node_addresses[head] = ans
        while curr:
            if curr.next:
                if curr.next not in node_addresses:
                    ans.next = Node(curr.next.val)
                    node_addresses[curr.next] = ans.next
                else:
                    ans.next = node_addresses[curr.next]
            else:
                ans.next = None

            if curr.random:
                if curr.random in node_addresses:
                    ans.random = node_addresses[curr.random]
                else:
                    ans.random = Node(curr.random.val)
                    node_addresses[curr.random] = ans.random

            curr = curr.next
            ans = ans.next
        return first_node
# @lc code=end
