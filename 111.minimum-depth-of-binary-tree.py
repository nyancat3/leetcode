#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Breadth-first search
        # time complexity: O(n), space complexity: O(n)
        # First loop is used for just calculation of depth, second loop is used to iterate all nodes, so Time Complexity would be O(n).
        # Since we have used one extra queue, so, the space complexity will be O(n).
        if not root:
            return 0
        que = deque([root])
        min_depth = 1
        while que:
            for i in range(len(que)):
                curr = que.popleft()
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                if not curr.left and not curr.right:
                    return min_depth
            min_depth += 1
        return min_depth

# @lc code=end
