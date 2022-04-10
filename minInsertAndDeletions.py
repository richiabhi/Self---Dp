def minIandD(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for _ in range(m+1)]for _ in range(n+1)]

    def lcs(s1, s2, n, m):
        if n == 0 or m == 0:
            return 0
        if dp[n][m] != -1:
            return dp[n][m]
        if s1[n-1] == s2[m-1]:
            dp[n][m] = 1+lcs(s1, s2, n-1, m-1)
            return dp[n][m]
        else:
            dp[n][m] = max(lcs(s1, s2, n-1, m), lcs(s1, s2, n, m-1))
            return dp[n][m]
    x = lcs(s1, s2, n, m)
    return (n+m)-2*x


print(minIandD(input(), input()))
