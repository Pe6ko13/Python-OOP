def solution():
    def integers():
        start = 1
        while True:
            yield start
            start += 1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        l = []
        for i in seq:
            if len(l) == n:
                return l
            l.append(i)

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
