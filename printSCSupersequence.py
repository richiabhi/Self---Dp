def printLCSupersequence(str1, str2):
    m = len(str1)
    n = len(str2)
    ans = ""
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            ans = str1[i-1]+ans
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                ans = str1[i-1]+ans
                i -= 1
            else:
                ans = str2[j-1]+ans
                j -= 1
    while i > 0:
        ans = str1[i-1]+ans
        i -= 1
    while j > 0:
        ans = str2[j-1]+ans
        j -= 1
    return ans


s1 = input()
s2 = input()
print(printLCSupersequence(s1, s2))
