def countSubsetWithK(n, arr, sum):
    dp = [[0 for _ in range(sum+1)]for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for j in range(1, sum+1):
        dp[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]


arr = [1, 1, 1, 1]
n = len(arr)
sum = 1
print(countSubsetWithK(n, arr, sum))
