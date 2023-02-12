# to print numbers from 1 to 5
i = 1

# while loop
while i <= 5:
    print(i, end=' ')  # avoiding newline instead adding space at the end of line
    i = i + 1
print("outside while")

# for loop
for i in range(1, 6):
    print(i, end=' ')
print("outside for")

# for loop with step +2
for i in range(1, 6, 2):
    print(i, end=' ')
print("outside for")

# trying to check what range function is returning
print(type(range(1, 6)))

# find number of digits in a number
num = 5013

if num == 0:
    num_digits = 1
else:
    num_digits = 0

n = num
while n > 0:
    num_digits = num_digits + 1
    n = n // 10
print(num, "has ", num_digits, " digits.")

# find number of digits in a number by converting to string
print(num, "has ", len(str(num)), " digits. <-- used to typecast to str to find len")
