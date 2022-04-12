import sys


class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[-1]*101 for i in range(501)]

        def solve(arr, i, j):
            if i >= j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            ans = sys.maxsize
            for k in range(i, j):
                temp = solve(arr, i, k) + solve(arr, k+1, j) +arr[i-1]*arr[k]*arr[j]
                ans = min(ans, temp)
                dp[i][j] = ans
            return dp[i][j]

        return solve(arr, 1, len(arr)-1)
