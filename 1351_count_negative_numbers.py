"""
Given a m * n matrix grid which is sorted in non-increasing order both
row-wise and column-wise.

Return the number of negative numbers in grid.

Example:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""
from typing import List


class Solution():
    def count_negatives(self, grid: List[List[int]]) -> int:
        count = 0
        for each_list in grid[::-1]:
            for item in each_list[::-1]:
                if item < 0:
                    count += 1
                else:
                    count += 1
                    break
        return count


obj = Solution()
grid = [[4, 3, 1, -4], [-1, -3, -5, -9], [9, 5, 3, 1]]
print(obj.count_negatives(grid))
