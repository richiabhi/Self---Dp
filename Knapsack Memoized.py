def knapsack(n, w, items, weight):
    if n == 0 or w == 0:
        return 0
    if memo[n][w] != -1:
        return memo[n][w]

    if weight[n-1] <= w:
        memo[n][w] = max(items[n-1]+knapsack(n-1, w-weight[n-1],
                         items, weight), knapsack(n-1, w, items, weight))
        return memo[n][w]
    else:
        memo[n][w] = knapsack(n-1, w, items, weight)
        return memo[n][w]


if __name__ == "__main__":
    n = 3
    A = [60, 100, 120]
    B = [10, 20, 30]
    capacity = 50
    memo = [[-1 for _ in range(capacity+1)]for _ in range(n+1)]
    print(knapsack(n, capacity, A, B))
