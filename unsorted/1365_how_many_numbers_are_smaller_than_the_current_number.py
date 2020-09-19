from typing import List
from collections import defaultdict


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        intuition for this approach is, after getting a sorted array.
        the index of each element shows the number of elements behind
        '''
        res = defaultdict(list)
        for index, element in enumerate(sorted(nums)):
            if element not in res:
                res[element] = index
        return [res[element] for element in res]

    def brute_force(self, nums: List[int]) -> List[int]:    
        res = []
        for index in range(len(nums)):
            val = nums[index]
            count = 0
            for jindex in range(len(nums)):
                if jindex != index:
                    if val > nums[jindex]:
                        count += 1
            res.append(count)
        return res


obj = Solution()
print(obj.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
