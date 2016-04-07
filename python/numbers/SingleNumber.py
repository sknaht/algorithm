class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        num = 0
        for i in range(len(A)):
            num ^= A[i]

        return num
