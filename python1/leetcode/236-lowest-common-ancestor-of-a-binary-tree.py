# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def find(node):
            if not node:
                return []
            found = []
            if node == p or node == q:
                found.append(node)
            for t in (node.left, node.right):
                found.extend(find(t))
                if len(found) == 2:
                    return found + [node]
                if len(found) > 2:
                    return found
            return found

        result = find(root)
        print result[-1].val


a = TreeNode(1)
b = TreeNode(2)
a.left = b
Solution().lowestCommonAncestor(a, a, b)
