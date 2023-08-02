# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target,
#   return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and
#   you may not use the same element twice.
# You can return the answer in any order.


def two_sum_brute_force(numbers, sum_target):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == sum_target:
                return [i, j]


# Example 1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
result = two_sum_brute_force([2, 7, 11, 15], 9)
print("[0,1] <==> ", result)
