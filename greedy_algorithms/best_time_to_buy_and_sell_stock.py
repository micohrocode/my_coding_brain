def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # always look for the new lowest price
        min_price = min(min_price, price)
        # check for new max profit each time
        max_profit = max(max_profit, price - min_price)

    return max_profit