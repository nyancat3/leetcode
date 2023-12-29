# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Breadth first search
        if not root:
            return []
        node_que = collections.deque([root])
        ans = []

        while node_que:
            ans.append([])
            for i in range(len(node_que)): # Cannot use node_que because left/right values will be appended in the loop
                node = node_que.pop() # Pop from right
                ans[-1].append(node.val)
                if node.left:
                    node_que.appendleft(node.left) # Append from left
                if node.right:
                    node_que.appendleft(node.right) # Append from left
        return ans
