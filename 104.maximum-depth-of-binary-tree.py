#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. recursive depth-first search
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # 2. breadth-first search
        # if not root:
        #     return 0
        # que = deque([root])
        # level = 0
        # while que:
        #     for i in range(len(que)):
        #         element = que.popleft()
        #         if element.left:
        #             que.append(element.left)
        #         if element.right:
        #             que.append(element.right)
        #     level += 1
        # return level

        # 3. iterative depth-first search
        res = 0
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
                res = max(res, depth)
        return res
# @lc code=end
