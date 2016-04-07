# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):

        stack = [root]
        visited = [[False, False]]
        res = []
        while len(stack) > 0:
            curr = stack[-1]
            if not curr:
                stack.pop()
                visited.pop()
                continue
            if not visited[-1][0] and curr.left:
                stack.append(curr.left)
                visited[-1][0] = True
                visited.append([False, False])
                continue
            if not visited[-1][1] and curr.right:
                stack.append(curr.right)
                visited[-1][1] = True
                visited.append([False, False])
                continue
            res.append(curr.val)
            stack.pop()
            visited.pop()
        return res
