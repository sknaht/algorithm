# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, curr, reversed = [], [root], False
        while curr:
            next, tmp = [], []
            for node in curr:
                if reversed:
                    tmp.insert(0, node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            curr, reversed = next, not reversed
            ans.append(tmp)
            
        return ans
