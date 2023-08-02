import array
import sys

int_array = array.array('i', [1, 2, 3])

for i in int_array:
    print(i, end=", ")

print()
print("the size of array [1, 2, 3] is", sys.getsizeof(int_array))

float_array = array.array('d', [1.1, 2.2, 3.3])
for d in float_array:
    print(d, end=", ")

print()
print("the size of array [1.1, 2.2, 3.3] is", sys.getsizeof(float_array))
