#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr:
            while curr: # go to the leftmost node
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()  # pop the leftmost node
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right   # if curr.right is None, the next iteration of the outer while loop will pop the next node from the stack
        return 0
# @lc code=end
