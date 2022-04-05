def countSubsetWithSumK(n, arr, target):
    if n == 0:
        return 0
    if target == 0:
        return 1
    if arr[n-1] > target:
        return countSubsetWithSumK(n-1, arr, target)
    take = countSubsetWithSumK(n-1, arr, target-arr[n-1])
    notTake = countSubsetWithSumK(n-1, arr, target)
    return take+notTake
