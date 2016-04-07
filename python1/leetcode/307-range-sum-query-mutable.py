class Node:
    def __init__(self, lower, upper):
        self.left = None
        self.right = None
        self.lower = lower
        self.upper = upper
        self.s = 0


class Tree:

    def __init__(self, lower, upper):
        self.root = Node(lower, upper)

    def update(self, i, delta):

        p = self.root
        p.s += delta
        while p.lower < p.upper:
            m = (p.lower + p.upper) / 2
            if i > m:
                if not p.right:
                    p.right = Node(m + 1, p.upper)
                p = p.right

            else:
                if not p.left:
                    p.left = Node(p.lower, m)
                p = p.left
            p.s += delta


    def range(self, i, j):


        def sumrange(node, lower, upper):

            if not node:
                return 0

            if lower <= node.lower and node.upper <= upper:
                return node.s

            s = 0

            m = (node.lower + node.upper) / 2

            if lower <= m:
                s += sumrange(node.left, lower, min(m, upper))
            if m < upper:
                s += sumrange(node.right, max(lower, m + 1), upper)

            return s


        return sumrange(self.root, i, j)




class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums

        self.tree = Tree(0, len(nums) - 1)
        for i in xrange(len(nums)):
            self.tree.update(i, nums[i])


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.tree.update(i, val - self.nums[i])
        nums[i] = val




    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.range(i, j)



        # Your NumArray object will be instantiated and called as such:

nums = [7,2,7,2,0]
numArray = NumArray(nums)
numArray.update(4,6)
numArray.update(0,2)
numArray.update(0,9)
numArray.update(3,8)

print numArray.sumRange(0,4 )
