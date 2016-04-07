class TreeNode(object):
    def __init__(self, number):
        self.number = number
        self.count = 1
        self.countsmaller = 0
        self.right, self.left = None, None

class BSTree(object):
    def __init__(self):
        self.root = None

    def insert(self, number):
        if self.root == None:
            self.root = TreeNode(number)
            return
        t = self.root
        parent = None
        while t:
            parent = t
            if number > t.number:
                t = t.right
            elif number < t.number:
                t.countsmaller += 1
                t = t.left
            else:
                t.count += 1
                return
        if number < parent.number:
            parent.left = TreeNode(number)
        else:
            parent.right = TreeNode(number)

    def delete(self, number):
        p = self.root
        parent = p
        while p:
            if p.number == number:
                p.count -= 1
                return
            elif p.number < number:
                p = p.right
            else:
                p.countsmaller -= 1
                p = p.left

    def query(self, lower, upper):
        s1 = 0
        s2 = 0

        for limit in [lower, upper]:
            s1 = 0
            p = self.root
            while p:
                if p.number <= limit:
                    s1 += p.countsmaller + p.count
                    p = p.right
                else:
                    p = p.left
            s1 -= s2
            s2 = s1

        return s1



class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        tree = BSTree()
        i = 0
        for x in nums:
            if tree.query(x-t-1, x+t) > 0:
                return True
            tree.insert(x)
            if i >= k:
                tree.delete(nums[i - k])
            i += 1

        return False



if __name__ == '__main__':
    print Solution().containsNearbyAlmostDuplicate([3,6,0,2],2,2)
