import numpy

# numpy.add
# numpy.subtract
# numpy.multiply (it's not same as dot product)
# numpy.dot
# scalar function add/substract/multiply 2 to all elements arr +/-/* 2

# sum of elements of
arr1 = numpy.array([1, 2, 3])
arr2 = numpy.array([1, 2, 3])
sum_arr1_2 = numpy.sum((arr1, arr2))
sums_arr1_and_2 = numpy.sum((arr1, arr2), axis=1)
print(sum_arr1_2, sums_arr1_and_2)


# numpy.zeros(2) => [0.0, 0.0]
# numpy.zeros(2,2) => [[0,0, 0,0], [0.0, 0.0]]
# numpy.ones(2, dtype=int8) => [1, 1]

print(numpy.full((2, 2), 6))  # [[6, 6], [6, 6]]
print(numpy.random.randint(6, size=(2, 2)))

print(numpy.identity(2, dtype='int8'))

#sin
print(numpy.sin(numpy.array([1, 2, 3])))
#linspace
print(numpy.linspace(0, 10, 5, dtype='int8')) #equi-spaced  5 points between 0 and 10 inclusive