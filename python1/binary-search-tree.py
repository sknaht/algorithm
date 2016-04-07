class TreeNode(object):

    def __init__(self, key, val):
        self.key, self.val, self.right, self.left = key, val, None, None


class BSTree(object):

    def __init__(self):
        self.root = None

    def __delete_min(self, node):
        if not node.left:
            return node.right
        node.left = self.__delete_min(node.left)
        return node

    def delete_min(self):
        self.root = self.__delete_min(self.root)

    def insert(self, node):
        if not self.root:
            self.root = node
            return
        t, parent = self.root, self.root
        while t:
            if t.key == node.key:
                t.val = node.val
                return
            elif t.key < node.key:
                parent = t
                t = t.right
            else:
                parent = t
                t = t.left
        if node.key > parent.key:
            parent.right = node
        else:
            parent.left = node

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        self.root = self.__delete_key(self.root, key)

    def __delete_key(self, node, key):
        """
        :type node: TreeNode, None
        """
        if not node:
            return None
        if node.key < key:
            node.right = self.__delete_key(node.right, key)
        elif node.key > key:
            node.left = self.__delete_key(node.left, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            t = node
            node = self.find_min(node.right)
            node.right = self.__delete_min(t.right)
            node.left = t.left
        return node

    def inorder_traverse(self):
        stack = []
        node = self.root
        while node:
            stack.append(node)
            node = node.left
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return result


if __name__ == '__main__':
    import random
    tree = BSTree()

    # ------------------  testing delete_min
    vs = set([])
    for i in xrange(50):
        x = random.randint(0, 100)
        vs.add(x)
        t = TreeNode(x, x)
        tree.insert(t)

    print tree.inorder_traverse()
    l = list(vs)
    l.sort()
    print l
    print len(l)
    print ''

    for i in xrange(len(l) / 2):
        tree.delete_min()
    l = tree.inorder_traverse()
    print l
    print len(l)
    print ''

    # ------------------  testing delete key
    vs = set([])
    tree = BSTree()
    for i in xrange(50):
        x = random.randint(0, 100)
        vs.add(x)
        t = TreeNode(x, x)
        tree.insert(t)

    print tree.inorder_traverse()
    l = list(vs)
    l.sort()
    print l
    print len(l)
    print ''

    for i in xrange(80):
        x = random.randint(0, 100)
        if x in vs:
            vs.remove(x)
        tree.delete(x)

    r = tree.inorder_traverse()
    print r
    l = list(vs)
    l.sort()
    print l

