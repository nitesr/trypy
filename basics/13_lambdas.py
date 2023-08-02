def add(a, b):
    return a + b


add_2 = lambda a, b: a + b

add_result = add(10, 20)
add_2_result = add_2(10, 20)
print("adding using add function (10, 20)", add_result)
print("adding using add lambda (10, 20)", add_2_result)
print("printing add function", add, "; type is", type(add))
print("printing add lambda", add_2, "; type is", type(add_2))

greeting = lambda: "Hello Amigo!"
print("calling greeting lambda", greeting())



