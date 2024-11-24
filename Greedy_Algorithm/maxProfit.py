# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以多次买卖股票。



def maxProfit(prices):
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))  # Output: 5