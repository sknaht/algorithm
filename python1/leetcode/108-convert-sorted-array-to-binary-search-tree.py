# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def generate(nums):
            if not nums:
                return None
            m = len(nums) / 2
            t = TreeNode(nums[m])
            t.left, t.right = generate(nums[:m]), generate(nums[m + 1:])
            return t

        return generate(nums)
