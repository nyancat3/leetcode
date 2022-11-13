#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # T O(n), S O(n)?
        if not root:
            return None
        l = root.left
        root.left = root.right
        root.right = l
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        # This code is fine as well. Don't need to return root.
        def recursive(node):
            if not node:
                return None
            l = node.left
            node.left = node.right
            node.right = l

            recursive(node.left)
            recursive(node.right)
            return None # Back to the stacked caller

        recursive(root)
        return root
# @lc code=end
