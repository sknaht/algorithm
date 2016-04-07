# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans, stack, visited, total, node = [], [], [], 0, root
        while node:
            stack.append(node)
            total += node.val
            node = node.left
        while stack:
            node = stack[-1]
            if not (node.left or node.right):
                if total == sum:
                    ans.append([x.val for x in stack])
            if node not in visited and node.right:
                visited.append(node)
                node = node.right
                while node:
                    stack.append(node)
                    total += node.val
                    node = node.left
            else:
                total -= stack.pop().val
        return ans


    def pathSum2(self, root, sum):

        ans = []

        def traverse(node, path, ans, total):
            if not node.left and not node.right:
                if total == sum:
                    ans.append([x for x in path])
                return
            if node.left:
                traverse(node.left, path + [node.left.val], ans, total + node.left.val)
            if node.rigth:
                traverse(node.right, path + [node.right.val], answ, total + node.right.val)

        if root:
            traverse(root, [root.val], ans, root.val)

        return ans
