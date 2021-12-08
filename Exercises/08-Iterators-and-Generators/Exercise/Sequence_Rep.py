class sequence_repeat:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.idx = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.num:
            if self.idx == len(self.seq):
                self.idx = 0
            self.idx += 1
            self.counter += 1
            return self.seq[self.idx - 1]
        raise StopIteration

        # idx, self.idx = self.idx, self.idx + 1
        # if idx == self.num:
        #     raise StopIteration
        # return self.seq[idx % len(self.seq)]




result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
