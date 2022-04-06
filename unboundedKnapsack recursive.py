def unboundedKnapsack(n, w, items, weights):
    if n == 0 or w == 0:
        return 0
    if weights[n-1] <= w:
        return max(items[n-1]+unboundedKnapsack(n, w-weights[n-1], items, weights), unboundedKnapsack(n-1, w, items, weights))
    else:
        return unboundedKnapsack(n-1, w, items, weights)


n = 4
items = [10, 40, 50, 70]
weights = [1, 3, 4, 5]
w = 8
print(unboundedKnapsack(n, w, items, weights))
