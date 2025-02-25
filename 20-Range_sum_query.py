# Question link => https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:
    def __init__(self, nums: List[int]):
        # Initialize a prefix sum array to store cumulative sums
        self.prefix = []
        cur = 0  # Variable to keep track of the running sum
        
        # Compute the prefix sum for the given array
        for n in nums:
            cur += n  # Add the current element to the running sum
            self.prefix.append(cur)  # Store the cumulative sum in the prefix array
            
    def sumRange(self, left: int, right: int) -> int:
        # Get the prefix sum up to the 'right' index
        rightSum = self.prefix[right]
        
        # Get the prefix sum up to the 'left - 1' index (to exclude elements before 'left')
        # If left is 0, there are no elements to exclude, so we take 0
        leftSum = self.prefix[left - 1] if left > 0 else 0
        
        # Return the sum of elements from index 'left' to 'right'
        return rightSum - leftSum
