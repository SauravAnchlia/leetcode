from functools import reduce 
from math import prod


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        s = 0
        for item in str(n):
            product *= int(item)
            s += int(item)
        return product - s


obj = Solution()
print(obj.subtractProductAndSum(523))
