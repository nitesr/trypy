import random

print("available functions in random module:", dir(random))

print("random between 1..20 :", random.randint(1, 20))
print("random between 0 .. 1 :", random.random())
print("random element from [1, 4, 6, 2, 8] :", random.choice([1, 4, 6, 2, 8]))
print("random element from Google :", random.choice("Google"))
list1 = [1, 4, 6, 2, 8]
random.shuffle(list1)
print("randomly shuffle list [1, 4, 6, 2, 8] :", list1)
print("randomly sample 2 elements from [1, 4, 6, 2, 8] :", random.sample(list1, 2))
