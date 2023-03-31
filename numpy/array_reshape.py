import numpy

int_1d_array = numpy.array([1, 2, 3, 4])
int_2d_array = numpy.array([1, 2, 3, 4], ndmin=2)
int_3d_array = numpy.array([1, 2, 3, 4], ndmin=3)
print("shape of 1d, 2d and 3d arrays is", int_1d_array.shape, int_2d_array.shape, int_3d_array.shape)

int_3d_array_1 = numpy.array([[[1, 2, 3, 4]]])
print("shape of int_3d_array_1 arrays is", int_3d_array_1.shape)

int_1d_array_reshape_to_2d = int_1d_array.reshape(2, 2)
int_1d_array_reshape_to_2d_1 = int_1d_array.reshape(1, 4)
print("shape of int_1d_array_reshape_to_2d array is", int_1d_array_reshape_to_2d.shape)
print(int_1d_array_reshape_to_2d)

# reshaped array is view over original array
int_1d_array_reshape_to_2d[0, 0] = 11
print("first element is modified in original array; 1 -> ", int_1d_array[0], int_1d_array_reshape_to_2d_1[0, 0])
int_1d_array[0] = 111
print("first element is modified in reshaped array; 11 -> ", int_1d_array_reshape_to_2d[0, 0], int_1d_array_reshape_to_2d_1[0, 0])
