from typing import List


class Solution:
    def max_satisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        
        always_satisfied = 0
        max_satisfied = 0
        local_satisfied = 0
        powerup_satisfied = 0
        
        for index in range(len(customers)):
            if grumpy[index] == 0:
                always_satisfied += customers[index]
                customers[index] = 0
        for index, customer_now in enumerate(customers):
            local_satisfied += customer_now
            if index >= x:
                local_satisfied -= customers[index - x]
            max_satisfied = max(max_satisfied, local_satisfied)
        

        return max_satisfied + always_satisfied

obj = Solution()
print(obj.max_satisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
