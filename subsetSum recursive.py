def subsetSum(n, arr, target):
    if n == 0:
        return False
    if target == 0:
        return True
    if arr[n-1] > target:
        return subsetSum(n-1, arr, target)
    return subsetSum(n-1, arr, target) or subsetSum(n-1, arr, target-arr[n-1])
