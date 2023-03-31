import numpy

int_array_1 = numpy.array([1, 2, 3])
int_array_2 = numpy.array([4, 5, 6])
int_array_1_2 = numpy.concatenate((int_array_1, int_array_2))
print("int_array_1_2 is", int_array_1_2)

# concatenated array is a new array
int_array_1_2[0] = 11
print("int_array_1[0] is not modified!", int_array_1[0])

int_array_2d_1 = numpy.array([[1, 2, 3], [4, 5, 6]])
int_array_2d_2 = numpy.array([[7, 8, 9], [10, 11, 12]])
int_array_2d_1_2_by_row = numpy.concatenate((int_array_2d_1, int_array_2d_2))
int_array_2d_1_2_by_col = numpy.concatenate((int_array_2d_1, int_array_2d_2), axis=1)
print("int_array_2d_1_2_by_row is 4x3: \n", int_array_2d_1_2_by_row)
print("int_array_2d_1_2_by_col is 3x4: \n", int_array_2d_1_2_by_col)


int_array_1_2_stack = numpy.stack((int_array_1, int_array_2))
print("int_array_1_2_stack is: \n", int_array_1_2_stack)

int_array_2d_1_2_stack_by_row =  numpy.stack((int_array_2d_1, int_array_2d_2))
print("int_array_2d_1_2_stack_by_row is: \n", int_array_2d_1_2_stack_by_row)

int_array_2d_1_2_stack_by_col = numpy.stack((int_array_2d_1, int_array_2d_2), axis=1)
print("int_array_2d_1_2_stack_by_col is: \n", int_array_2d_1_2_stack_by_col)