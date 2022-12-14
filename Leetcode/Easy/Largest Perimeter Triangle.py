# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Example 2:

# Input: nums = [1,2,1]
# Output: 0
 

# Constraints:

# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106

# Solution

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        max_sum=0
        n=len(nums)
        nums.sort(reverse=True)
        for i in range(0,n-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                max_sum=max(max_sum,nums[i]+nums[i+1]+nums[i+2])
                break
            else:
                max_sum=0
        return max_sum