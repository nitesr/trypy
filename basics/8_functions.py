# Functions

def add(a, b):
    return a + b


print("2 + 3 <==>", add(2, 3))

# built-in functions
list1 = [2, 5, 3, 8]
str1 = "Google"

print("max element in list1 is ", max(list1))
print("min element in list1 is ", min(list1))
print("len of list1 is ", len(list1))

print("max char in str1 is ", max(str1))
print("min char in str1 is ", min(str1))
print("len of str1 is ", len(str1))

x = -5
print("absolute value of -5 is ", abs(x))
print("2^10 is ", pow(2, 10))
print("14 in binary format is ", bin(14))

# binary literal assignment to int variable
a = 0b1110
print(type(a), a)
