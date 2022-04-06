def countSubsetWithK(n, arr, sum):
    dp = [[0 for _ in range(sum+1)]for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]


def main(nums, target):
    n = len(nums)
    su = sum(nums)
    val = abs(su+target)//2
    if ((su-target) % 2 == 1) or (target > su):
        return 0
    return countSubsetWithK(n, nums, val)


print(main([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
