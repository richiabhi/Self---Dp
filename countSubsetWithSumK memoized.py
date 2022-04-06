def countSubsetWithSumK(n, arr, target):
    if n == 0:
        return 0
    if target == 0:
        return 1
    if dp[n][target] != -1:
        return dp[n][target]
    if arr[n-1] > target:
        dp[n][target] = countSubsetWithSumK(n-1, arr, target)
        return dp[n][target]
    dp[n][target] = countSubsetWithSumK(
        n-1, arr, target-arr[n-1]) + countSubsetWithSumK(n-1, arr, target)
    return dp[n][target]


if __name__ == "__main__":
    arr = [1, 1, 1, 1]
    n = len(arr)
    target = 1
    dp = [[-1 for _ in range(target+1)]for _ in range(n+1)]
    print(countSubsetWithSumK(n, arr, target))
