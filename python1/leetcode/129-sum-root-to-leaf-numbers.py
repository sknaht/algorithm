# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack, visited, node, curr, total = [], [], root, 0, 0
        while node:
            stack.append(node)
            curr = curr * 10 + node.val
            node = node.left

        while stack:
            node = stack[-1]
            if not (node.left or node.right):
                total += curr
            if node not in visited and node.right:
                visited.append(node)
                node = node.right
                while node:
                    stack.append(node)
                    curr = curr * 10 + node.val
                    node = node.left
            else:
                stack.pop()
                curr /= 10
        return total

