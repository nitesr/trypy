# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Given an integer array nums, return the greatest common divisor of
#   the smallest number and largest number in nums.
#
# The greatest common divisor of two numbers is the largest positive integer
#   that evenly divides both numbers.

# Solution:
#   using Ecluid's GCD algorithm
#       for a given two number m & n where m > n, the GCD(m, n) = GCD(n, m%n)  = n when m%n == 0)
#           GCD(m, n) == GCD(m-n, n) (assuming m-n > n) or GCD(n, m-n) (assuming m-n < n) or n if (m == n)
#                   say GCD(m, n) is g i.e. g.p = m and g.q = n where p > q
#                   (m-n) = (g.p - g.q) = g.(p-q) = g.r i.e. GCD of m, n & m-n is g.
#                   hence, GCD(m, n) == GCD(m-n, n) == GCD(m-n, m)
#          GCD(m, n) == GCD(m-2n, n) (assuming m-2n > n) or GCD(n, m-2n) (assuming m-2n < n) or n if (m == 2n)
#         GCD(m, n) == GCD(m-xn, n) (assuming m-xn > n) or GCD(n, m-xn) (assuming m-xn < n) or n if (m == xn)
#        max value of x is the highest quotient which get n closer to m & m-xn is the remainder i.e m%n
#        so, GCD(m-xn, n) == GCD(n, m%n)
#    for example m = 16 & n = 36
#       GCD(36, 16) == GCD(16, 36%16) == GCD(16, 4) == GCD(4, 16%4) == GCD(4, 0) == 4
#
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
