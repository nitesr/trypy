# https://leetcode.com/problems/count-primes/
# Given an integer n, return the number of prime numbers that are strictly less than n.

def count_primes_by_number_theory(n) -> int:
    if n < 2:
        return 0

    is_prime_array = [True for i in range(0, n)]  # boolean list
    is_prime_array[0] = False
    is_prime_array[1] = False

    i = 2
    while i * i <= n:  # checking till sqrt(n)
        if is_prime_array[i]:
            for j in range(i * i, n, i):  # checking from i * i e.g. For i=3 -> 1 x 3, 2 x 3 is covered for i = [1, 2]
                is_prime_array[j] = False
        i = i + 1

    primes_count = 0
    for is_prime in is_prime_array:
        if is_prime:
            primes_count = primes_count + 1

    return primes_count


# Example 1:
#   Input: n = 10
#   Output: 4
#   Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
result = count_primes_by_number_theory(10)
print("4 <==>", result)

# Example 2:
#   Input: n = 0
#   Output: 0
result = count_primes_by_number_theory(0)
print("0 <==>", result)

# Example 3:
#   Input: n = 1
#   Output: 1
result = count_primes_by_number_theory(1)
print("0 <==>", result)
