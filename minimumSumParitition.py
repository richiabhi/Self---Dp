import sys


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
    return dp[n]


arr = [1, 4]
n = len(arr)
target = sum(arr)
dp = isSubsetSum(n, arr, target)
array = []
for i in range(target//2 + 1):
    if dp[i]:
        array.append(i)
mini = sys.maxsize
for i in range(len(array)):
    mini = min(mini, target-2*array[i])
print(mini)
