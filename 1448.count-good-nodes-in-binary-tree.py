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
        ans = 0
        def isGoodNode(node: TreeNode, max_num: int):
            nonlocal ans
            if not node:
                return
            if node.val >= max_num:
                ans += 1
                print(node.val)
            max_num = max(max_num, node.val)
            isGoodNode(node.left, max_num)
            isGoodNode(node.right, max_num)
        isGoodNode(root, root.val)
        return ans
# @lc code=end
