class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, node, ans, visited = [], root, [], []
        while node:
            stack.append(node)
            node = node.left
        while stack:
            if stack[-1] not in visited and stack[-1].right:
                visited.append(stack[-1])
                node = stack[-1].right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                ans.append(stack.pop().val)
        return ans