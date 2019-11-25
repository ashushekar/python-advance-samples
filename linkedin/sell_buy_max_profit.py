class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        result = 0
        prices = iter(prices)
        minSofar = next(prices)
        for price in prices:
            minSofar = min(price, minSofar)
            result = max(result, price-minSofar)
        return result