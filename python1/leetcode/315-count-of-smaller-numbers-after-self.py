class TreeNode(object):

    def __init__(self, num):
        self.num = num
        self.smaller = 0
        self.left = None
        self.right = None


class Solution(object):

    def countSmaller(self, nums):
        def insert(node, root, result):
            if not root:
                return node
            if node.num < root.num:
                root.left = insert(node, root.left, result)
                root.smaller += 1
            else:
                root.right = insert(node, root.right, result)
                result[0] += root.smaller
                if root.num != node.num:
                    result[0] += 1
            return root

        root = None
        result = []
        for i, num in enumerate(nums[::-1]):
            result.insert(0, 0)
            root = insert(TreeNode(num), root, result)

        return result


print Solution().countSmaller([1,1])