class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_num = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < 0:
            raise StopIteration

        val_to_return = self.current_num
        self.current_num -= 1
        return val_to_return


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")