from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = prices[0]
        low = prices[0]
        profit = 0
        for price in prices:
            if price < low:
                print(f'Price is {price} . low is {low}')
                print(f'Profit is {profit}')
                low = price
                high = 0
            elif price > high:

                print(f'Price is {price} . high is {high}')
                print(f'Profit is {profit}')
                if profit < (price - low):
                    profit = price - low
        return profit


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
