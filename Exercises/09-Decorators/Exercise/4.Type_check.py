def type_check(type_):
    def decor(func):
        def wrapper(x):
            if isinstance(x, type_):
                return func(x)
            else:
                return "Bad Type"
        return wrapper
    return decor





@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
