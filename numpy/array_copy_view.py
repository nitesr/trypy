import numpy

int_1d_array = numpy.array([1, 2, 3, 4, 5, 6, 7])
int_1d_array_copy = int_1d_array.copy()
int_1d_array_view = int_1d_array.view()

int_1d_array[0] = 2
print("pos 0 element on copy vs view is ", int_1d_array_copy[0], int_1d_array_view[0])

int_1d_array_view[0] = 3
print("pos 0 element on copy vs view is ", int_1d_array_copy[0], int_1d_array_view[0])



