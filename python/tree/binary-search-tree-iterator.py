# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack != []

    # @return an integer, the next smallest number
    def next(self):
        tmp = self.stack.pop()
        t = tmp.right
        while t:
            self.stack.append(t)
            t = t.left
        return tmp.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(7)
x = t.right
x.left = TreeNode(4)
x.right = TreeNode(8)
x.left.left = TreeNode(3)
x.left.right = TreeNode(6)
x.left.right.left = TreeNode(5)

x = BSTIterator(t)
while x.hasNext():
    print x.next()