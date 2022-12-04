#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time Complexity O(n)
        # Worst Space Complexity O(n). Height of the tree, so if the tree is balanced, O(log n) but if the tree is one-sided O(n)
        ans = 0

        def diameter(node):
            nonlocal ans    # Enable to substitute values to a global value
            if not node:
                return 0
            l = diameter(node.left)
            r = diameter(node.right)
            ans = max(ans, l + r)   # Calc the answer diameter
            return max(l, r) + 1    # Return the height of this sub tree

        diameter(root)
        return ans
# @lc code=end
