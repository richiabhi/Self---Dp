def unboundedKnapsack(n, w, items, weights):
    if n == 0 or w == 0:
        return 0
    if dp[n][w] != -1:
        return dp[n][w]
    if weights[n-1] <= w:
        dp[n][w] = max(items[n-1]+unboundedKnapsack(n, w-weights[n-1],
                       items, weights), unboundedKnapsack(n-1, w, items, weights))
        return dp[n][w]
    else:
        dp[n][w] = unboundedKnapsack(n-1, w, items, weights)
        return dp[n][w]


n = 4
items = [10, 40, 50, 70]
weights = [1, 3, 4, 5]
w = 8
dp = [[-1 for _ in range(w+1)]for _ in range(n+1)]
print(unboundedKnapsack(n, w, items, weights))
