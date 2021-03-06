# neetcodes solution using something called kadanes alogrithm
def maxProfit(prices):
    res = 0

    l = 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
    return res