class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.i = 0
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.count:
            raise StopIteration()
        self.i += 1
        p = self.start
        self.start += self.step
        return p



numbers = take_skip(2, 6)
for number in numbers:
    print(number)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
