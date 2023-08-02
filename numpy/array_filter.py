import numpy

int_array = numpy.array([1, 2, 3])
bool_array = [True, False, True]
filtered_int_array = int_array[bool_array]
print(filtered_int_array, end=", ")
print(type(filtered_int_array))

filter_cond = int_array < 3
print(type(filter_cond))
filter_cond_int_array = int_array[filter_cond]
print(filter_cond_int_array, end=", ")