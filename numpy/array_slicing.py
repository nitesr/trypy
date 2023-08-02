import numpy

int_1d_array = numpy.array([1, 2, 3, 4, 5, 6, 7])
print("slice of int_1d_array from pos 2 to 4 is", int_1d_array[2:5])
print("slice of int_1d_array from pos 4 till end is", int_1d_array[4:])
print("slide of int_1d_array from ", int_1d_array[-3:-1])


int_2d_array = numpy.array([[1, 2, 3], [4, 5, 6]])
print("slice of int_2d_array from pos 2 to 3 of first row is", int_2d_array[0, 1:3])
print("slice of int_2d_array from pos 2 to 3 of second row is", int_2d_array[1:, 1:3])
print("slice of int_2d_array from pos 2 to 3 of both rows is", int_2d_array[0:, 1:3])