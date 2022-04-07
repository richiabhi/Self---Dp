def cutRod(n, price):
    length = [x for x in range(1, n+1)]
    dp = [[-1 for _ in range(n+1)]for _ in range(n+1)]

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
    return unboundedKnapsack(n, n, price, length)


n = 8
price = [3, 5, 8, 9, 10, 17, 17, 20]
print(cutRod(n, price))
