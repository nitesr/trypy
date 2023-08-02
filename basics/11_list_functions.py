list1 = [1, 4]

list1.append(10)
list1.append(20)

print([1, 4], " -> after appending 10 & 20 ->", list1)

list2 = [30, 40]
list1.extend(list2)
print([1, 4, 10, 20], " -> after extending with another list [30, 40] ->", list1)

list1.insert(2, 5)
print([1, 4, 10, 20, 30, 40], " -> insert 5 at pos 2 -> ", list1)

animals = ["cat", "dog", "fish", "dog"]
animals.remove("dog")
print("after removing a dog", animals)

# error on removing an non-existing animal
# animals.remove("giraffe")

languages = ["english", "telugu", "hindi", "french", "spanish"]
languages.pop(3)
print("after removing 3rd element", languages)
languages.pop()
print("after removing last element", languages)

prime_numbers = [2, 3, 5, 7, 9, 11]
del prime_numbers[0:3]
print("after removing 0,1,2 elements", prime_numbers)
del prime_numbers
# error after deleting the list, prime_numbers doesn't exist!
# print("after deleting all elements", prime_numbers)

original_list = [0, 1, 2, 3, 4, 5]
sub_list = original_list[2:5]
print("list slicing", sub_list)
sub_list.clear()
print("after removing all elements", sub_list)

odd_list = original_list[1::2]
print("odd pos list slicing: ", odd_list)
print("get penultimate element using negative index: ", odd_list[-2])


