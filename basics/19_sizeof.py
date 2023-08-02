import sys

a = 10**9
print("size of", a, "in bytes is ", sys.getsizeof(a))

big_a = 10**18
print("size of", big_a, "in bytes is ", sys.getsizeof(big_a))

bigger_a = 10**26
print("size of", bigger_a, "in bytes is ", sys.getsizeof(bigger_a))

str = "a"
print("size of a in bytes is ", sys.getsizeof(str))

str1 = "ab"
print("size of ab in bytes is ", sys.getsizeof(str1))
