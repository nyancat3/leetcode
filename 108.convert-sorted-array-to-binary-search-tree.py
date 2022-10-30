#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int):
            if left > right:
                return None

            # If make a left node as a root, round down by //
            middle = (left + right) // 2
            # If make a right node as a root, round up by math.ceil
            # middle = math.ceil((left + right) / 2)
            root = TreeNode(nums[middle])
            root.left = helper(left, middle -1)
            root.right = helper(middle + 1, right)
            return root

        return helper(0, len(nums) - 1)
# @lc code=end
