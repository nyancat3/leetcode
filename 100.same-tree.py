#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time complexity O(p + q)
        # Space Complexity: The recursive method depends on the height of the tree, the worst case is O(N), best case is O(logN) https://racla.github.io/100-Same-Tree/
        if not p and not q:
            return True
        elif not p or not q:    # Only one of them is not None means they are not equal
            return False
        res = (p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
        print(res)
        return res
# @lc code=end
