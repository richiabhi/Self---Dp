def climbstairs(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = climbstairs(n-1)+climbstairs(n-2)
    return dp[n]


n = int(input())
dp = [-1 for _ in range(n+1)]
print(climbstairs(n))
