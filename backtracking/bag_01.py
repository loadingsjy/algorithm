

# 0-1 bag problem

# Given a bag of n items, we need to divide it into two bags of equal size such that the total weight of each bag is the same. We can either take the first item or the last item of the bag. We need to find the minimum number of items that we need to take from the bag to divide it into two bags of equal weight.

# Approach:
# We can solve this problem using dynamic programming. Let's define dp[i][j] as the minimum number of items that we need to take from the first i items to divide them into two bags of equal weight, where the weight of each bag is j.

# Base case:
# dp[0][j] = 0, dp[i][0] = inf, where i >= 1 and j >= 1


# Recursive case:
# If we take the first item, then we need to divide the remaining items into two bags of equal weight, where the weight of each bag is j/2.
# If we take the last item, then we need to divide the remaining items into two bags of equal weight, where the weight of each bag is (j-1)/2.
# We take the minimum of these two options.


# Time complexity: O(n^2)
# Space complexity: O(n^2)


def bag_problem(n, j):
    dp = [[float('inf') for _ in range(j+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1, n+1):
        for j in range(1, j+1):
            if i == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + 1
    return dp[n][j]


# Example:
# n = 4, j = 3
# dp = [[inf, inf, inf, inf],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 0]]
# The minimum number of items that we need to take from the first 4 items to divide them into two bags of equal weight is 0.  
