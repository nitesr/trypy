import numpy

int_array = numpy.array([1, 2, 3, 4])
#numpy.split
print(numpy.split(int_array, 2))  # splits into two element arrays
print(numpy.split(int_array, [1, 3]))  # splits into three arrays [0], [1,2], [3]

#numpy.array_split
print(numpy.array_split(int_array, 3)) # splits into two array without throwing error [0, 1] [2], [3]