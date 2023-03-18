# can't change value, delete tuple, add to tuple

tuple_1 = ("Max", 28, "New York")
tuple_2 = "Mini", 27, "New York" # Paranthesis are optional; tuple with a single element should have , at end
tuple_3 = 29,
print(type(tuple_3))
print(tuple_1)
print(tuple_2)
print(tuple_3)

# error: can't modify tuple
#tuple_1[0] = "Maxie"

# convert from iterable (list, dict, string)
tuple_from_list = tuple([1,2,3])
tuple_from_string = tuple("abc")
print(tuple_from_list)
print(tuple_from_string)

#iterate over tuple
for i in tuple_1:
    print("tuple_1", i)

if "New York" in tuple_1:
    print("Yes New York is in tuple_1 -> ",tuple_1)
else:
    print("Yes New York is not in tuple_1 -> ", tuple_1)

my_tuple = tuple("apple")
print("my_tuple is", my_tuple)

# len of tuple
print("length of my_tuple is", len(my_tuple))

# count of element in tuple
print("count of 'p' in my_tuple is", my_tuple.count("p"))

# index of element in tuple
print("index of first 'p' in my_tuple is", my_tuple.index("p"))
print("index of first 'p' in my_tuple from 2-3 sub-tuple is", my_tuple.index("p", 2, 3))

# error x is not in tuple
# print("index of first 'x' in my_tuple is", my_tuple.index("x"))

# repetition
my_rep_tuple = ('a', 'b') * 2
print("my_rep_tuple is", my_rep_tuple)




