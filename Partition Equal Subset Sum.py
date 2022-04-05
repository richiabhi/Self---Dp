def isSubsetSum(n, arr, sum):
    dp = [[False for i in range(sum + 1)]for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, sum + 1):
        dp[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i - 1][j-arr[i-1]]
    return dp[n][sum]


def equalPartition(n, arr):
    su = sum(arr)
    if su % 2 != 0:
        return False
    return isSubsetSum(n, arr, su//2)


arr = [1, 2, 3, 5]
n = len(arr)
print(equalPartition(n, arr))
