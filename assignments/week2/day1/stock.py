
prices = [7, 1, 5, 3, 6, 4]

def maxProfit(prices):
    # we keep track of the lowest price first
    # then move our r ptr to find the day to sell it the highest
    # dynamic sized sliding window

    l, max_gains = 0, 0
    
    for r in range(len(prices)):
        if prices[r] < prices[l]:
            l = r
            max_gains = max(max_gains, prices[r] - prices[l])
    return max_gains
