def knapsack(n, w, items, weight):
    if n == 0 or w == 0:
        return 0
    if weight[n-1] <= w:
        return max(items[n-1]+knapsack(n-1, w-weight[n-1], items, weight), knapsack(n-1, w, items, weight))
    else:
        return knapsack(n-1, w, items, weight)


if __name__ == "__main__":
    n = 3
    A = [60, 100, 120]
    B = [10, 20, 30]
    capacity = 50
    print(knapsack(n, capacity, A, B))
