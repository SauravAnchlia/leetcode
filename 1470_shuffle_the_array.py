from typing import List


class solution():
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        sol = []
        for number in range(0, len(nums)-n):
            sol.extend([nums[number], nums[number+n]])
        return sol

    def shuffle_with_zip(self, num: List[int], n: int) -> List[int]:
        sol = []
        for first, second in zip(num[0:n], num[n:]):
            sol.extend([first, second])
        return sol


obj = solution()
print(obj.shuffle([2, 5, 1, 3, 4, 7], 3))
print(obj.shuffle_with_zip([2, 5, 1, 3, 4, 7], 3))
