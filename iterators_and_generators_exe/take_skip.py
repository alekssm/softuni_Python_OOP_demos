class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0
        self.element = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.element == self.count:
            raise StopIteration
        num_to_return = self.num
        self.num += self.step
        self.element += 1
        return num_to_return
        

numbers = take_skip(2, 6)
for number in numbers:
    print(number)