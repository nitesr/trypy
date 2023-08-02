# https://leetcode.com/problems/three-divisors/
# Given an integer n, return true if n has exactly three positive divisors.
#   Otherwise, return false.
# An integer m is a divisor of n if there exists an integer k such that n = k * m.
# Constraints:
#   1 <= n <= 10^4

def has_three_divisors_only(n) -> bool:
    # 1 & n will be factors for any number, so we already have 2
    #    for one more it has to be the same number squared to equal to n
    #    and this number shouldn't be further factored i.e. it should be prime.
    #    sqrt(n) should be a prime
    # since n < 10^4, sqrt(n) is a prime less than 100
    primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    for p in primes_under_100:
        if p * p == n:
            return True
    return False


# Example 1:
#   Input: n = 2
#   Output: false
#   Explanation: 2 has only two divisors: 1 and 2.
result = has_three_divisors_only(2)
print("False <==>", result)

# Example 2:
#   Input: n = 4
#   Output: true
#   Explanation: 4 has three divisors: 1, 2, and 4.
result = has_three_divisors_only(4)
print("True <==>", result)

# Example 3:
#   Input: n = 9
#   Output: true
#   Explanation: 9 has three divisors: 1, 3, and 9.
result = has_three_divisors_only(9)
print("True <==>", result)

# Example 4:
#   Input: n = 64
#   Output: false
#   Explanation: 64 has 7 divisors: 1, 2, 4, 8, 16, 32 and 64.
result = has_three_divisors_only(64)
print("False <==>", result)
