import functools

list_numbers = [1, 2, 3, 4]
map_square_numbers = map(lambda a: a * a, list_numbers)
map_pow_numbers = map(pow, list_numbers, list_numbers)
print("map_square_numbers", map_square_numbers, type(map_square_numbers))
print("list of squares of ", list_numbers, " is", list(map_square_numbers))
print("powers of themselves list", list_numbers, " is", list(map_pow_numbers))

lambdas = [lambda a: a * a, lambda a: a + a]
list_after_applying_lambdas_on_10 = list(map(lambda f: f(10), lambdas))
print("list_after_applying_lambdas_on_10", list_after_applying_lambdas_on_10)

scores = [10, 34, 59, 76, 89, 99]
scores_over_75 = list(filter(lambda s: s > 75, scores))
print("scores > 75 from scores", scores, "is", scores_over_75)
print("sum of all scores > 75", scores, "is", functools.reduce(lambda a, b: a + b, scores_over_75))
