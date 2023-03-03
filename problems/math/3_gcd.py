# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Given an integer array nums, return the greatest common divisor of
#   the smallest number and largest number in nums.
#
# The greatest common divisor of two numbers is the largest positive integer
#   that evenly divides both numbers.

# Solution:
#   GCD(Greatest Common Divisor) for a given two numbers is a
#   number when it divides them it leaves them as co-prime
#   i.e. there are no other common factors between them other
#   than 1.
#
#   Examples:
#   GCD(10, 5) is 5 as 10/5=5 and 5/5=1 and there is no
#   common factor between 5 and 1 other than 1.
#
#   GCD(10, 8) is 2 as 10/2=5 and 8/2=4 and there is no common
#   factor between 5 and 4 other than 1.
#
#   How do we compute it for a given numbers m, n where m >= n?
#     We can try all possibilities from n to 1 and check
#     which divides both m and n. This is an exhaustive
#     approach with time complexity of O(n). Can we do
#     better ?
#
#     There is Euclid's theorem to find the GCD and it takes
#     logx(n) time. We can leverage that.
#     He states,
#
#     Theorem:
#         I.   GCD(m, n) = GCD(n, m%n) where m > n
#         II.  GCD(m, n) = n where m == n
#         III. GCD(m, n) = m where m >= n and n == 0
#
#     Proof:
#         Case I:
#         Say,  GCD(m, n) = g, where m > n
# 	    => m = g x p , n = g x q
#         => m-n = g (p - q) = g x r
#         => m-2n = g (p - 2q) = g x s  (where m > 2n)
#         => GCD(m-xn, n) = g, where (m-xn) > n
#         => GCD(n, m-x`n), where (m-x`n) < n
#
#         m > n => m = x`n + y (x` is quotient and y is
#             remainder. y < n)
#         => m-x`n = y => y = m-x`n < n
#         => the lowest value of m-x`n is remainder of m, n
#         => GCD(n, m-x`n) = GCD(n, m%n)
#         => GCD(m, n) = GCD(n, m%n)
#           example m = 16 & n = 36
#           GCD(36, 16) == GCD(16, 36%16) == GCD(16, 4) == GCD(4, 16%4) == GCD(4, 0) == 4
#
#         Case II:
#             since m == n, the greatest number it can
#             divide is itself. so m is the GCD
#             => GCD(m, n) = m, where m == n
#
#         Case III:
#             Given n is 0 and m > 0. any number when
#             divides 0 is 0. the greatest number it can
#             divide 0 is maximum of m & 0 => m i.e. 0/m = 0
#             => GCD(m, n) = m, where n == 0
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
