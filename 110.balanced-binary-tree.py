#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time complexity O(n)
        # Worst Space Complexity O(n). Height of the tree, so if the tree is balanced, O(log n) but if the tree is one-sided O(n)
        def balanced_height(node):
            if not node:
                return 0
            l = balanced_height(node.left)
            r = balanced_height(node.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            height = max(l, r) + 1
            return height

        return balanced_height(root) != -1

        # Below is a naive approach
        # Time Complexity O(n)*n = O(n^2)
        # def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #     if not root:
        #         return True
        #     if abs(self.height(root.left) - self.height(root.right)) > 1:
        #         return False
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)

        # def height(self, root):
        #     if not root:
        #         return 0
        #     return 1 + max(self.height(root.left), self.height(root.right))
# @lc code=end
