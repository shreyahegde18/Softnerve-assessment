def Profit(prices):
    if len(prices) <= 1:
        return 0
    
    min_price = prices[0]  # Initialize the minimum price
    max_profit = 0  # Initialize the maximum profit
    
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]  # Update the minimum price
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price  # Update the maximum profit
    
    return max_profit

# Test case
prices = [7,1,5,3,6,4]
result = Profit(prices)
print(result)  # Output: 5

