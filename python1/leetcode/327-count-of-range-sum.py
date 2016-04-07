"""

class TreeNode:

    def __init__(self, number):
        self.countbigger = 0
        self.countself = 1
        self.number = number
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, number):
        if not self.root:
            self.root = TreeNode(number)
            return

        p = self.root
        parent = None
        while p:
            parent = p
            if number < p.number:
                p = p.left
            elif number > p.number:
                p.countbigger += 1
                p = p.right
            else:
                p.countself += 1
                return
        if number < parent.number:
            parent.left = TreeNode(number)
        elif number > parent.number:
            parent.right = TreeNode(number)

    def query_bigger(self, number):
        p = self.root
        s = 0
        while p:
            if number <= p.number:
                s += p.countself + p.countbigger
                p = p.left
            else:
                p = p.right
        return s



class Solution(object):
    def countRangeSum(self, nums, lower, upper):

        tree = Tree()

        s = 0

        y1 = 0
        y2 = 0
        lower -= 1
        for x in nums:
            tree.insert(s)
            s += x
            y1 += tree.query_bigger(s - lower)
            y2 += tree.query_bigger(s - upper)

        return max(0, y2 - y1)



if __name__ == "__main__":
    pass

"""




class BIT:

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (1 + n)

    def update(self, k, v):
        while k <= self.n:
            self.bit[k] += v
            k += -k & k

    def query(self, k):
        r = 0
        while k > 0:
            r += self.bit[k]
            k -= -k & k
        return r


def binary_search_index(sorted_list, key):
    l, r = 0, len(sorted_list)
    while l < r:
        m = (l + r) / 2
        if key < sorted_list[m]:
            r = m
        else:
            l = m + 1
    return r - 1


class Solution(object):
    def countRangeSum(self, nums, lower, upper):

        prefix_sum = set()
        s = 0
        for num in nums:
            prefix_sum.add(s)
            s += num
        prefix_sum.add(s)

        # generate the sorted prefix sum list without duplicate element
        prefix_sum = [None] + sorted(list(prefix_sum))

        # construct initial bit
        bit = BIT(len(prefix_sum) - 1)
        s = 0
        bit.update(binary_search_index(prefix_sum, s), 1)
        for num in nums:
            s += num
            bit.update(binary_search_index(prefix_sum, s), 1)

        s = 0
        result = 0
        for i in xrange(len(nums)):
            bit.update(binary_search_index(prefix_sum, s), -1)
            k = binary_search_index(prefix_sum, s + upper)
            result += bit.query(k)
            k = binary_search_index(prefix_sum, s + lower - 1)
            result -= bit.query(k)
            s += nums[i]

        return result


if __name__ == "__main__":
    print Solution().countRangeSum([10, -11, -1, 0], -1, 0)

