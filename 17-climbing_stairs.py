# Question link => https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:  # Edge case: If there's only 1 step, there's only 1 way to climb
            return 1
        
        dp = [0] * (n + 1)  # Create a DP array
        dp[1] = 1  # Only 1 way to climb 1 step
        dp[2] = 2  # Two ways to climb 2 steps: (1+1) or (2)
        
        # Fill the DP array using recurrence relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Ways to reach step i
        
        return dp[n]  # Return the number of ways to reach step n
