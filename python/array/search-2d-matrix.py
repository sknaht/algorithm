class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):

        if not matrix:
            return False

        def findonrow(row, left, right):
            while left <= right:
                mid = (left + right) / 2
                tmp = matrix[row][mid]
                if tmp == target:
                    return True
                if tmp > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        def find(left, right, up, down):
            if left > right or up > down:
                return False
            row, col = (up + down) / 2, (left + right) / 2
            if findonrow(row, left, right):
                return True

            if row > 0 and matrix[row - 1][col] >= target and find(left, col, up, row - 1):
                return True
            if col + 1 < len(matrix[0]) and row > 0 and matrix[up][col + 1] <= target <= matrix[row - 1][right] \
                and find(col + 1, right, up, row - 1):
                return True

            if row + 1 < len(matrix) and matrix[row + 1][left] <= target <= matrix[down][right] \
                and find(left, right, row + 1, down):
                return True

            return False

        return find(0, len(matrix[0]) - 1, 0, len(matrix) - 1)


print Solution().searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 10)