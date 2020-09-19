from collections import defaultdict 
from typing import List


class Solution:

    def count_ones(self, number: int, count_of_ones: List[int]) -> None:
        if number in (count_of_ones):
            return count_of_ones[number]
        else:
            for item in range(len(count_of_ones) - 1, number + 1):
                count_of_ones[item]=(count_of_ones[item >> 1] + (item & 1))
            return count_of_ones[number]
        
    def sortByBits(self, arr: List[int]) -> List[int]:
        count_of_ones = defaultdict(int)
        sorted_arr = defaultdict(list)
        for item in arr:
            count_of_ones[item] = self.count_ones(item, count_of_ones)
            sorted_arr[count_of_ones[item]].append(item)
        res = []
        print(sorted_arr)
        for item in sorted_arr.values():
            for num in sorted(item):
                res.append(num)
        return res


obj = Solution()
input = [1024,512,256,128,64,32,16,8,4,2,1]
print(obj.sortByBits(input))
print(obj.sortByBits([0,1,2,3,4,5,6,7,8]))