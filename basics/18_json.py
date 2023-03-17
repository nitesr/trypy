import json

person = {"name": "John", "age": 30, "salary": 100000, "married": False}
person_json = json.dumps(person)
print(person_json, "; whose type is", type(person_json))
print(json.dumps(person, indent=2), "; with indent")

person_obj = json.loads(person_json)
print(person_obj, "of type", type(person_obj))


class Laptop:
    def __init__(self, processor, ram, hdd):
        self.processor = processor
        self.ram = ram
        self.hdd = hdd


laptop_1 = Laptop("Intel", "4G", "256G")
print("Laptop obj json is", json.dumps(laptop_1.__dict__))
