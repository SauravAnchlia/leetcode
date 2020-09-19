from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int)
                        -> List[bool]:        
        res = []
        m = sorted(candies)[-1]
        for child in candies:
            r = True if child+extraCandies >= m else False 
            res.append(r)
        return res 