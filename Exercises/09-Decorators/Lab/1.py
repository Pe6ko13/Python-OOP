def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner
#
#
# @smart_divide
def divide(a, b):
    print(a/b)
#
#
new = smart_divide(divide)
new(2, 5)

# divide(2, 5)






# from time import time
#
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print(end - start)
#         return result
#     return wrapper
#
# @measure_time
# def some_func(*args, **kwargs):
