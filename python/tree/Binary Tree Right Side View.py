"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        def getview(node, result, d):
            if d > len(result):
                result.append(node.val)
            else:
                result[d] = node.val
            getview(node.left, result, d+1)
            getview(node.right, result, d+1)

        result = []
        getview(root, result, 0)
        return result
