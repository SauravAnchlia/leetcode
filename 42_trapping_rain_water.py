from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # the pointer to track the height of the left side 
        left_max = 0 
        # the pointer to track the height of the right side
        right_max = 0
        # left pointer
        left = 0
        # right pointer
        right = len(height) - 1
        water_trapped = 0
        # When we increment left and decrement right, we need an exit condition
        # which is when left crosses right
        while left < right:
            # if height of left is less than height of right
            # it becomes the bounding condition, hence we calculate w.r.t left
            if height[left] < height[right]:
                # update the left side everytime we encounter something bigger
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
        return water_trapped


obj = Solution()
print(obj.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
