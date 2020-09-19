from typing import List

# WIP


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = []
        return min(self.min_cost(cost, n-1, dp), self.min_cost(cost, n-2, dp))

    def min_cost(self, cost: List[List], n: int, dp: List[int]) -> int:
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return cost[n]
        if n in dp:
            return dp[n]
        dp[n] = cost[n] + min(self.min_cost(cost, n-1, dp),
                              self.min_cost(cost, n-2, dp))
        return dp[n]


obj = Solution()
print(obj.minCostClimbingStairs([10, 15, 20]))
print(obj.minCostClimbingStairs([0, 1, 1, 1]))
