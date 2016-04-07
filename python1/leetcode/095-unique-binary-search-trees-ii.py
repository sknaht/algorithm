# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate(nums):
            if not nums:
                return [None]
            curr = []
            for i in xrange(len(nums)):
                left = generate(nums[:i])
                right = generate(nums[i + 1:])
                for ltree in left:
                    for rtree in right:
                        t = TreeNode(nums[i])
                        t.left, t.right = ltree, rtree
                        curr.append(t)
            return curr

        return generate(range(1, n + 1))
