# Note: From Python 3.7, the dicts are ordered maps

person_max_dict = {"name": "Max", "age": 29, "city": "New York"}
print(type(person_max_dict))
print("person_max_dict is ", person_max_dict)
print("age of person_max_dict is ", person_max_dict["age"])
person_max_dict["age"] = 30
print("age of person_max_dict after 30th birthday is ", person_max_dict["age"])

# Using dict function to create dictionary
person_max_using_dict_func = dict(name="Max", age=29, city="New York")
print(type(person_max_using_dict_func))
print("person_max_using_dict_func is ", person_max_dict)

capital_cities_by_country = {"Nepal": "Kathmandu", "India": "Delhi", "Japan": "Tokyo"}
print("capital of Japan is ", capital_cities_by_country["Japan"])
capital_cities_by_country["USA"] = "Washington"  # adding a new key-value
print("capital of USA is ", capital_cities_by_country["USA"])
print("capital_cities_by_country is ", capital_cities_by_country)  # ordered by insertion order
del capital_cities_by_country["Nepal"]
print("After deleting Nepal, capital_cities_by_country is ", capital_cities_by_country)

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("squares is ", squares)
# KeyError as 6 doesn't exist in dict
# print("square of 6 is ", squares[6])
if 2 in squares:
    print("square of 2 is ", squares[2])

# loop over dict
for n in squares:
    print("square of ", n, "is", squares[n])
for key in squares.keys():
    print("square of ", key, "is", squares[key])
for value in squares.values():
    print(value)
for key, value in squares.items():
    print("square of ", key, "is", value)

# Using tuple as key with immutable elements
max_tuple = ("Max", 29, "New York")
mini_tuple = ("Mini", 27, "New York")
gpas_by_person = {max_tuple: 4.5, mini_tuple: 5}
print("gpas_by_person", gpas_by_person)
print("Max's gpa is", gpas_by_person[max_tuple])





