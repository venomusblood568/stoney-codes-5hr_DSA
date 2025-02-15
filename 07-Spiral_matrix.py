# Question Link => https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            # Remove and add first row
            ret += matrix.pop(0)

            # Remove last column
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # Remove last row (reversed)
            if matrix:
                ret += matrix.pop()[::-1]

            # Remove first column (fixing the issue)
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))

        return ret
