from typing import List


class solution:
    def greedy(self, nums: List) -> bool:
        last = len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            if index + nums[index] >= last:
                last = index

        return True if last == 0 else False

    def can_jump(self, nums: List) -> bool:
        return self.recursive(nums, 0)

    def recursive(self, nums: List, index: int) -> bool:
        if index == len(nums) - 1:
            return True
        longest_jump = min(index + nums[index], len(nums) - 1)
        for jindex in range(longest_jump, index, -1):
            if self.recursive(nums, jindex):
                return True
        return False

    def can_jump_topdown(self, nums: List[int]) -> bool:
        lookup = {}
        return self.recur(nums, 0, lookup)

    def top_down(self, nums: List[int], index: int, lookup) -> bool:
        if index == len(nums) - 1:
            lookup[index] = True
            return lookup[index]

        if index in lookup:
            return lookup[index]
        longest_jump = min(index + nums[index], len(nums) - 1)
        for jindex in range(longest_jump, index, -1):
            if self.recur(nums, jindex, lookup):
                lookup[jindex] = True
                return lookup[jindex]

        lookup[index] = False
        return lookup[index]


obj = solution()
val = obj.greedy([2, 3, 1, 1, 4])
print(val)
