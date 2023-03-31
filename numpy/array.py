import sys
import numpy

int_0d_array = numpy.array(1)  # by default the size is int64
print(int_0d_array)
print("type of int_1d_array is", type(int_0d_array))
print("byte size of int_1d_array is", sys.getsizeof(int_0d_array))
print("array properties: \n",
      "size: ", int_0d_array.size, "\n",
      "shape: ", int_0d_array.shape, "\n",
      "dimension: ", int_0d_array.ndim, "\n",
      "data-type: ", int_0d_array.dtype, "\n")

int_1d_array = numpy.array([1, 2, 3], dtype="int8")  # by default the size is int64
print(int_1d_array)
print("type of int_1d_array is", type(int_1d_array))
print("byte size of int_1d_array is", sys.getsizeof(int_1d_array))
print("array properties: \n",
      "size: ", int_1d_array.size, "\n",
      "shape: ", int_1d_array.shape, "\n",
      "dimension: ", int_1d_array.ndim, "\n",
      "data-type: ", int_1d_array.dtype, "\n")

int_2d_array = numpy.array([[1, 2, 3], [4, 5, 6]], dtype="int8")
print(int_2d_array)
print("type of int_3d_array is", type(int_2d_array))
print("byte size of int_3d_array is", sys.getsizeof(int_2d_array))
print("int_2d_array properties: \n",
      "size: ", int_2d_array.size, "\n",
      "shape: ", int_2d_array.shape, "\n",
      "dimension: ", int_2d_array.ndim, "\n",
      "data-type: ", int_2d_array.dtype, "\n")
print("0,1 element of int_2d_array is", int_2d_array[0][1], int_2d_array[0, 1])

int_3d_array = numpy.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(int_3d_array)
print("type of int_3d_array is", type(int_3d_array))
print("byte size of int_3d_array is", sys.getsizeof(int_3d_array))
print("int_3d_array properties: \n",
      "size: ", int_3d_array.size, "\n",
      "shape: ", int_3d_array.shape, "\n",
      "dimension: ", int_3d_array.ndim, "\n",
      "data-type: ", int_3d_array.dtype, "\n")
print("0,1,1 element of int_3d_array is", int_3d_array[0][1][1], int_3d_array[0, 1, 1])

# loop
print("looping int_2d_array:")
for i in int_2d_array:
    for j in i:
        print(j, end=", ")
    print()

print("looping int_2d_array using nditerator:")
for i in numpy.nditer(int_2d_array):
    print(i, end=", ")

print("looping int_2d_array using ndenumerator:")
for idx, i in numpy.ndenumerate(int_2d_array):
    print("index=", idx, " and value=", i, end=", ")
