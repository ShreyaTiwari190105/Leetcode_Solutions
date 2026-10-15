class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        ans = 0

        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n - 1 - i]

        if n % 2 == 1:
            mid = n // 2
            ans -= mat[mid][mid]

        return ans