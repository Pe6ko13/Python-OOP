# def get_primes(numbers):
#     for num in numbers:
#         if num < 2:
#             continue
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#         if is_prime:
#             yield num


def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    if number < 2:
        return False
    return True


def get_primes(seq):
    return (x for x in seq if is_prime(x))


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))