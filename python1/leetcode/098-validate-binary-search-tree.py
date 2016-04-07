# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        
        prev = None
        while stack:
            node = stack.pop()
            if prev and prev.val >= node.val:
                return False
            prev = node
            if node.right:
                stack.append(node.right)
                node = node.right.left
                while node:
                    stack.append(node)
                    node = node.left
        return True        
            