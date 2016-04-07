class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        p = 1
        while p < len(nums):
            p = p * 2
        self.tree = [0] * p * 2

        self.nodenum = p

        for i in xrange(len(nums)):
            self.tree[p + i] = nums[i]

        p /= 2
        while p > 0:
            for i in xrange(p):
                t = i + p
                self.tree[t] = self.tree[2 * t] + self.tree[2 * t + 1]
            p /= 2



    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        t = self.nodenum + i
        delta = val - self.tree[t]

        while t > 0:
            self.tree[t] += delta
            t /= 2


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        i = i + 1
        j = j + 1

        def sumrange(tree, node, lower, upper, node_lower, node_upper):

            if lower <= node_lower and node_upper <= upper:
                return tree[node]

            s = 0
            m = (node_upper + node_lower) / 2

            if lower <= m:
                s += sumrange(tree, node * 2, lower, min(m, upper), node_lower, m)
            if m < upper:
                s += sumrange(tree, node * 2 + 1, max(m, lower), upper, m + 1, node_upper)

            return s

        return sumrange(self.tree, 1, i, j, 1, self.nodenum)



        # Your NumArray object will be instantiated and called as such:

nums = [7,2,7,2,0]
numArray = NumArray(nums)
numArray.update(1,6)
numArray.update(0,2)
numArray.update(0,9)
numArray.update(3,8)

print numArray.sumRange(0,4)
