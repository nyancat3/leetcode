#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time Complexity O(root * subRoot)
        # Worst Space Complexity O(root + subRoot)? Since the call stack could hold at max height of root + height of subRoot function calls

        # Not necessary because the number of nodes in subRoot is 1 or more.
        # if not subRoot:
        #     return True
        if not root:
            return False
        if self.is_same_tree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def is_same_tree(self, r, s):
        if not r and not s:
            return True
        elif not r or not s:
            return False
        return (r.val == s.val and
                self.is_same_tree(r.left, s.left) and
                self.is_same_tree(r.right, s.right))

# @lc code=end
