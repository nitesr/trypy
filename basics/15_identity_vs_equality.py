str_a = "Hello"
str_b = "Hello"
str_c = "Hello1"
# both identities will be same as python will pool the literals
print("identity of str_a is", id(str_a), "and that of str_b is", id(str_b))
print("identity of str_c is", id(str_c))

print("str_a is str_b", (str_a is str_b))
print("str_a == str_b", (str_a == str_b))


class OurPerson:
    name = None
    age = None

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


person_1 = OurPerson('Hello', 10)
person_2 = OurPerson('Hello', 10)
print("person_1 is person_2", (person_1 is person_2))
print("person_1 == person_2", (person_1 == person_2))
