x = 10
y = 15

# greater than
gresult = x > y
print(x, " > ", y, " = ", gresult)
print("xx", " > ", "y", " = ", ("xx" > "y"))

# greater than equal to
geresult = x >= y
print(x, " >= ", y, " = ", geresult)
print("xx", " >= ", "y", " = ", ("xx" >= "y"))

# less than
lresult = x < y
print(x, " < ", y, " = ", lresult)
print("xx", " < ", "y", " = ", ("xx" < "y"))

# less than equal to
leresult = x <= y
print(x, " <= ", y, " = ", leresult)
print("xx", " <= ", "y", " = ", ("xx" <= "y"))

# not equal to
neresult = x != y
print(x, " != ", y, " = ", neresult)
print("xx", " != ", "y", " = ", ("xx" != "y"))

# equal to
eresult = x == y
print(x, " == ", y, " = ", eresult)
print("xx", " == ", "xx", " = ", ("xx" == "xx"))

a = True
b = False
# and
print(a, " and ", b, " = ", (a and b))
# or
print(a, " or ", b, " = ", (a or b))
# not
print(" not ", b, " = ", (not b))
