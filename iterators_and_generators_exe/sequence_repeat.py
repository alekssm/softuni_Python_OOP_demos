class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.general_index = 0
        self.str_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.general_index == self.number:
            raise StopIteration

        if self.str_index == len(self.sequence):
            self.str_index = 0

        letter = self.sequence[self.str_index]
        self.str_index += 1
        self.general_index += 1
        return letter


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')