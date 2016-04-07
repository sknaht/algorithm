class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        if preorder == '#':
            return True


        a = preorder.split(",")

        stack = []
        if a[0] != '#':
            stack.append(a.pop(0))
            visited = [0]

        for x in a:
            if not stack:
                return False
            visited[-1] += 1
            if x == '#':
                while visited and visited[-1] == 2:
                    stack.pop()
                    visited.pop()
            else:
                stack.append(x)
                visited.append(0)

        return not stack

if __name__ == "__main__" :
    print Solution().isValidSerialization("#")









