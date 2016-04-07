"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        '''
        # using stack for O(n) space, time O(n)
        curr = root
        stack = []
        ans = [None, None]
        while curr:
            stack.append(curr)
            curr = curr.left
        prev = None
        while stack:
            curr = stack.pop()
            if prev and prev.val > curr.val:
                if not ans[0]:
                    ans[0] = prev
                ans[1] = curr

            t = curr.right
            while t:
                stack.append(t)
                t = t.left
            prev = curr
        ans[0].val, ans[1].val = ans[1].val, ans[0].val
        '''


        # morris traverse, space O(1), time > O(n)

        curr = root
        ans = [None, None]
        prev = None

        def check(prev, curr):
            if prev and prev.val > curr.val:
                if not ans[0]:
                    ans[0] = prev
                ans[1] = curr

        while curr:
            if not curr.left:
                check(prev, curr)
                prev = curr
                curr = curr.right
            else:
                tmp = curr.left
                while tmp.right and tmp.right != curr:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = curr
                    curr = curr.left
                else:
                    check(prev, curr)
                    tmp.right = None
                    prev = curr
                    curr = curr.right

        ans[0].val, ans[1].val = ans[1].val, ans[0].val


t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(7)
x = t.right
x.left = TreeNode(4)
x.right = TreeNode(8)
x.left.left = TreeNode(3)
x.left.right = TreeNode(6)
x.left.right.left = TreeNode(5)


Solution().recoverTree(t)


