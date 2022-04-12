import sys


def MCM(arr, i, j):
    if i >= j:
        return 0
    ans = sys.maxsize
    for k in range(i, j):
        temp = MCM(arr, i, k)+MCM(arr, k+1, j)+(arr[i-1]*arr[k]*arr[j])
        ans = min(temp, ans)
    return ans


n = 5
arr = [40, 20, 30, 10, 30]
print(MCM(arr, 1, n-1))
