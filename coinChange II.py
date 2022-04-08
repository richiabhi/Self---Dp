def coinChange(coins, amount):
    n = len(coins)
    dp = [[-1 for _ in range(amount+1)]for _ in range(n+1)]

    def helperFunction(n, arr, amount):
        if amount == 0:
            return 1
        if n == 0:
            return 0
        if dp[n][amount] != -1:
            return dp[n][amount]
        if arr[n-1] <= amount:
            dp[n][amount] = helperFunction(
                n-1, arr, amount)+helperFunction(n, arr, amount-arr[n-1])
            return dp[n][amount]
        else:
            dp[n][amount] = helperFunction(n-1, arr, amount)
            return dp[n][amount]
    return helperFunction(n, coins, amount)


coins = [1, 2, 5]
amount = 5
print(coinChange(coins, amount))
