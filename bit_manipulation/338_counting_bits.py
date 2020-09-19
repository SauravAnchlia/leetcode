from typing import List

'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
'''

# bit manipulation
# medium
# link : https://leetcode.com/problems/counting-bits/



class Solution:
    def countBits(self, nums: int) -> List[int]:
        res = [0]
        for number in range(1, nums + 1):
            res.append(res[number >> 1] + (number & 1))
        return res


    def naive_countBits(self, nums: int) -> List[int]:
        res = []
        for number in range(nums + 1):
            count = 0
            while number:
                if number & 1 :
                    count += 1
                number >>= 1 
            res.append(count)
        return res

obj = Solution()
print(obj.countBits(4))

