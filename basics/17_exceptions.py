import traceback

int_a = 0
int_b = 10

try:
    int_div = int_b // int_a
    print(int_div)
except ZeroDivisionError as e:
    print("ZeroDivisionError!", e)
    print(e.__traceback__)
    traceback.print_exception(e)
except Exception as e:
    print("error!", e)
finally:
    print("in final")

print("outside of try")