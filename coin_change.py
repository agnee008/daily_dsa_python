"""
dp[i] represents the minimum number of coins needed to make amount i.
The array is initialized to amount + 1 for all indices because amount + 1 is a value larger than 
any possible number of coins needed (since it's impossible to need more than amount coins to make 
up amount using coins of at least denomination 1).
The value amount + 1 is used as a placeholder to represent infinity or an unreachable state.
dp[0] is set to 0 because no coins are needed to make an amount of 0.
"""


def coinChange(coins: list[int], amount:int):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for a in range(1, amount+1):
        for c in coins:
            if a - c> 0 :
                dp[a] = min(dp[a], 1+dp[a-c])
    return dp[amount] if dp[amount] != 1 + amount else -1