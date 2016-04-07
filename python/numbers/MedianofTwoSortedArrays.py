class Solution:
    # @return a float

    def findMedianSortedArrays(self, A, B):

        def find_kth(A, B, k):
            if len(A) > len(B):
                return find_kth(B, A, k)
            if not A:
                return B[max(k-1,0)]
            if k == 1:
                if A[0] > B[0]:
                    return B[0]
                else:
                    return A[0]
            i = max(min(len(A), k/2), 1)
            j = max(k/2 - i, 1)
            if A[i-1] > B[j-1]:
                return find_kth(A, B[j:], k-j)
            else:
                return find_kth(A[i:], B, k-i)

        l = len(A) + len(B)
        m = find_kth(A, B, (l+1)/2)
        if l % 2 == 0:
            m = float(m + find_kth(A, B, (l+1)/2 + 1))/2
        return m

if __name__ == "__main__":
    t = Solution()
    print t.findMedianSortedArrays([1,1,3,3], [1,1,3,3])