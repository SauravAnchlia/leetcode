from typing import List 


class Solution:
    def binary_search(self, nums : List[int], key, left, right) -> int:
        if left > right :
            return -1

        mid = (left + right) //2
        
        if key == nums[mid]:
            return mid
        elif key < nums[mid]:
            return self.binary_search(nums, key, left, mid - 1)
        else:
            return self.binary_search(nums, key, mid + 1, right)
        

obj = Solution()
nums  = [1,5,8,15,19,23]
print(obj.binary_search(nums, 1, 0 , len(nums)))
