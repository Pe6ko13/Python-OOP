def even_parameters(function):
    def wrapper(*args):
        try:
            not_even = [x for x in args if not x % 2 == 0]
            if not_even:
                return 'Please use only even numbers!'
        except TypeError:
            return 'Please use only even numbers!'
        return function(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))
