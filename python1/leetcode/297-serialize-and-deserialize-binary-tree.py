# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    '''
    using preorder
    '''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = []
        stack = []

        def put(node):
            while node:
                s.append(str(node.val))
                stack.append(node)
                node = node.left
            s.append('#')

        put(root)
        while stack:
            put(stack.pop().right)
        return ','.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#':
            return None

        s = data.split(',')

        root = TreeNode(int(s.pop(0)))
        stack = [root]
        visited = [0]

        for x in s:
            parent = stack[-1]
            visited[-1] += 1
            if x == '#':
                while visited and visited[-1] == 2:
                    visited.pop()
                    stack.pop()
            else:
                node = TreeNode(int(x))
                if visited[-1] == 1:
                    parent.left = node
                else:
                    parent.right = node
                stack.append(node)
                visited.append(0)
        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    codec = Codec()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    s =  codec.serialize(root)

    node = codec.deserialize(s)

    print s
