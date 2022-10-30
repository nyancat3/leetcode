#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # iterative depth-first search
        if not root:
            return False
        stack = [[root, root.val]]
        while stack:
            node, sum = stack.pop()
            if node.left:
                stack.append([node.left, sum + node.left.val])
            if node.right:
                stack.append([node.right, sum + node.right.val])
            if not node.left and not node.right and sum == targetSum:
                return True
        return False

        # recursive depth-first search
        def helper(node, curSum):
            if not node:
                return False
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            return helper(node.left, curSum) or helper(node.right, curSum)

        return helper(root, 0)
# @lc code=end
