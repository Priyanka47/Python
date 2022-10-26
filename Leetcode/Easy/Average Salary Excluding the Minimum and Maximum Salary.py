# 1491. Average Salary Excluding the Minimum and Maximum Salary

# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

# Solution

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.pop(0)
        return sum(salary)/len(salary)