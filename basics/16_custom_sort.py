import dataclasses
import functools

points = [[1, 2], [3, 9], [4, 16], [5, 25], [4, 1]]
points_sorted = list(points)
points_sorted.sort()
print("default sort of points", points, "is", points_sorted)
points_sorted_by_y = list(points)
points_sorted_by_y.sort(key=lambda p: p[1])
print("sort of points by y", points, "is", points_sorted_by_y)


@dataclasses.dataclass
class Employee:
    name: str
    age: int
    salary: int


list_employees = [Employee('John', 30, 100000),
                  Employee('John', 31, 100000),
                  Employee('Joe', 31, 100000),
                  Employee('Adam', 35, 200000)]
list_employees_sort_by_name = list(list_employees)
list_employees_sort_by_name.sort(key=lambda e: e.name)
print("sort by name", list_employees_sort_by_name)

list_employees_sort_by_age = list(list_employees)
sorted(list_employees_sort_by_age, key=lambda e: e.age)
print("sort by age", list_employees_sort_by_age)

alpha_cmp = lambda str1, str2: 0 if str1 == str2 else 1 if str1 > str2 else -1
num_cmp = lambda num1, num2: num1-num2
emp_cmp = lambda e1, e2: e1.age-e2.age if e1.name == e2.name else alpha_cmp(e1.name, e2.name)

list_employees_sort_by_name_then_age = list(list_employees)
list_employees_sort_by_name_then_age.sort(key=functools.cmp_to_key(emp_cmp))
print("sort by name then age", list_employees_sort_by_name_then_age)

