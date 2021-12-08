def genrange(start, finish):
    # while start <= finish:
    #     yield start
    #     start += 1

    for i in range(start, finish + 1):
        yield i

# genrange = lambda start, finish: range(start, finish + 1)

print(list(genrange(1, 10)))

