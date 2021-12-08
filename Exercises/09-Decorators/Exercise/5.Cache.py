import time


def exec_time(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end = time.time()
        res = end - start_time
        return res
    return wrapper


def cache(func):
    def wrap(n):
        result = func(n)
        wrap.log[n] = result
        return result
    wrap.log = {}
    return wrap


@cache
@exec_time
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
for i in range(30):
    pass
print(f'Total time: {fibonacci(i)}')

fibonacci(4)
print(fibonacci.log)
