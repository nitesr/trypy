# dynamic array, arraylist, vector
list1 = [1, 2, 3, 4]

for element in list1:
    print(element, end=" ")
print(" <-- used element in list")

for i in range(0, len(list1)):
    print(list1[i], end=" ")
print(" <-- used index to iterate through list")

# list can be heterogeneous
hetro_list = [1, 1.2, "str", True]
for element in hetro_list:
    print(element, end=" ")
print(" <-- heterogeneous list")
