"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):

        def construct(ir, pr):
            if ir[0] > ir[1] or pr[0] > pr[1]:
                return None
            root_val = postorder[pr[0]]
            root_node = TreeNode(root_val)
            c = 0
            for i in xrange(ir[0], ir[1] + 1):
                if inorder[i] == root_val:
                    root_node.left = construct((ir[0], i - 1), (pr[0] + 1, pr[0] + c) )
                    root_node.right = construct((i + 1, ir[1]), (pr[0] + c + 1, pr[1]))
                    return root_node
                c += 1

        return construct((0, len(inorder) - 1), (0, len(postorder) - 1))


root = Solution().buildTree([4, 2,5,1, '#', 3,6], [4,5,2,'#',6,3,1])

def printout(root):
    if not root:
        return
    print root.val
    printout(root.left)
    printout(root.right)

printout(root)
