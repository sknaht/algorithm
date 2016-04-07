"""
 Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if not s1:
            return True
        n = len(s1)
        result = [[[False for i in xrange(n)] for i in xrange(n)] for i in xrange(n + 1)]

        for i in xrange(n):
            for j in xrange(n):
                if s1[i] == s2[j]:
                    result[1][i][j] = True

        for i in xrange(2, n + 1):
            for j in xrange(n - i + 1):
                for k in xrange(n - i + 1):
                    for t in xrange(1, i):
                        if result[t][j][k] and result[i-t][j+t][k+t] or result[i-t][j+t][k] and result[t][j][k + i - t]:
                            result[i][j][k] = True
                            break

        return result[n][0][0]


class Solution2:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        def recursiveFind(str1,str2):

            if sorted(str1)!=sorted(str2):
                return False

            if str1==str2:
                return True

            if len(str1)<=3:  # scramble can reach all permutation for length<=3
                return True

            for i in range(len(str1)-1):
                tmp1=str1[:i+1]
                tmp2=str1[i+1:]
                tmp3=str2[:i+1]
                tmp4=str2[i+1:]
                tmp5=str2[len(str1)-(i+1):]
                tmp6=str2[:len(str1)-(i+1)]

                if (recursiveFind(tmp1,tmp3) and recursiveFind(tmp2,tmp4)):
                    return True
                if (recursiveFind(tmp1,tmp5) and recursiveFind(tmp2,tmp6)):
                    return True

            return False

        return recursiveFind(s1, s2)

print Solution().isScramble("pcighfdjnbwfkohtklrecxnooxyipj", "npodkfchrfpxliocgtnykhxwjbojie")
