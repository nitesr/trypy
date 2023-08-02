import math

print("available functions in math module:", dir(math))

print("log base10 of 10^4 is ", math.log10(10000), math.log(1000, 10))

print("ceil of 5.3 is", math.ceil(5.3))
print("floor of 5.3 is", math.floor(5.3))
print("gcd of 6, 4 is", math.gcd(6, 4))

print("sqrt of 2 is", math.sqrt(2))

# print("sqrt of 2 is", math.isqrt(2))  # integer sqrt, supported from 3.8 version

# area of circle of 5 radius
print("area of circle with radius 5", math.pi * 5 * 5)
