from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for item in nums:
            sum += item
            result.append(sum)
        return result


obj = Solution()
result = obj.runningSum([1, 2, 3, 4])

print(result)
