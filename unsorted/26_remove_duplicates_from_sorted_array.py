from typing import List

'''
Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.
'''


class solution():
    def remove_duplicate(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        pointer = 0

        for index in range(0, len(nums)):
            if nums[index] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[index]

        print(nums)
        return pointer


obj = solution()
print(obj.remove_duplicate([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
``