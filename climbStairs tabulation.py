def climbStairsTab(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(climbStairsTab(n))
