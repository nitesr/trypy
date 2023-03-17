# Problem: Generate all prime numbers smaller than or equal to a given number.
# Examples:
#   Input: n = 5
#   Output: [2, 3, 5]
# Constraints:
#   1 <= value of given number <= 10^6

import unittest


def generate_prime_numbers(n):
    """
    Args:
     n(int32)
    Returns:
     list_int32
    """
    # Using Sieve of Eratosthenes algo
    #  for  2, 3, 4, 5, 6, 7, 8, 9, 10
    #   for 2 -> strike off 4, 6, 8, 10. so we have [2, 3, 5, 7, 9]
    #   for 3 -> strike off 6, 9. so we have [2, 3, 5, 7]
    #   for 4 -> strike off 8. so we have [2, 3, 5, 7]
    #   5 > sqrt(10) so stop here and collect non struck numbers i.e. [2, 3, 5, 7]

    # Write your code here.
    if n < 2:
        return []

    is_prime = [True for i in range(n + 1)]
    is_prime[1] = False

    i = 2
    while (i * i) < (n + 1):
        if is_prime[i]:
            for j in range(i + i, n + 1, i):
                is_prime[j] = False
        i = i + 1

    primes = []
    for r in range(2, n + 1):
        if is_prime[r]:
            primes.append(r)

    return primes


class Testcase(unittest.TestCase):
    def test_example1(self):
        input = 5
        result = generate_prime_numbers(input)
        self.assertEqual([2, 3, 5], result, "example case")

    def test_lessThan2(self):
        input = 1
        result = generate_prime_numbers(input)
        self.assertEqual([], result, "lessThan2 case")

    def test_biggerNumber(self):
        input = 20
        result = generate_prime_numbers(input)
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], result, "biggerNumber case")