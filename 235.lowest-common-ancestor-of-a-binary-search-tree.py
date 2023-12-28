# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time complexity: O(log n), Space: O(1)
        while True:
            current_val = root.val
            if current_val > p.val and current_val > q.val:
                root = root.left
            elif current_val < p.val and current_val < q.val:
                root = root.right
            else:
                return root
