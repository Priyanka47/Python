# 1523. Count Odd Numbers in an Interval Range

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Solution

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2==0 and high%2==0:
            return (high-low)//2
        else:
            return (high-low)//2 + 1