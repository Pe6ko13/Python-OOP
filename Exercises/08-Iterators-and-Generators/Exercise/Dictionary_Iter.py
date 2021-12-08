class dictionary_iter:
    def __init__(self, diction):
        self.dict = diction
        # self.__dict = iter(self.dict.items())

        self.length = len(self.dict)
        self.keys = list(self.dict.keys())
        self.current_index = 0

    def __iter__(self):
        return self

    # def next(self):
        # return next(self.__data)

    def __next__(self):
        if self.current_index >= self.length:
            raise StopIteration()
        key = self.keys[self.current_index]
        value = self.dict[key]
        self.current_index += 1
        return (key, value)



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
