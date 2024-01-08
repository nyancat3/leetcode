#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        def countGoodNodes(node: TreeNode, max_num: int):
            res = 0
            if not node:
                return 0
            if node.val >= max_num:
                res = 1
            max_num = max(max_num, node.val)
            res += countGoodNodes(node.left, max_num)
            res += countGoodNodes(node.right, max_num)
            return res
        return countGoodNodes(root, root.val)
# @lc code=end
