# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Given an integer array nums, return the greatest common divisor of
#   the smallest number and largest number in nums.
#
# The greatest common divisor of two numbers is the largest positive integer
#   that evenly divides both numbers.

def find_gcd_by_number_theory(num1, num2):
    small_number = min([num1, num2])
    big_number = max([num1, num2])
    while small_number > 0:
        remainder = big_number % small_number
        big_number = small_number
        small_number = remainder
    return big_number


def find_gcd(numbers):
    return find_gcd_by_number_theory(min(numbers), max(numbers))


# Example 1:
#   Input: nums = [2,5,6,9,10]
#   Output: 2
#   Explanation:
#       The smallest number in nums is 2.
#       The largest number in nums is 10.
#       The greatest common divisor of 2 and 10 is 2.
result = find_gcd([2, 5, 6, 9, 10])
print("2 <==>", result)

# Example 2:
#   Input: nums = [7,5,6,8,3]
#   Output: 1
#   Explanation:
#       The smallest number in nums is 3.
#       The largest number in nums is 8.
#       The greatest common divisor of 3 and 8 is 1.
result = find_gcd([7, 5, 6, 8, 3])
print("1 <==>", result)
