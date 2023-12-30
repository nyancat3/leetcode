#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        node_que = collections.deque([root])

        while node_que:
            node_val = 0
            for i in range(len(node_que)):
                node = node_que.popleft()
                node_val = node.val
                if node.left:
                    node_que.append(node.left)
                if node.right:
                    node_que.append(node.right)
            ans.append(node_val)
        return ans
# @lc code=end
