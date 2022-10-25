class vowels:
    _VOWELS = ["a", "e", "o", "i", "u", "y"]

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            if self.text[self.index].lower() in self._VOWELS:
                letter = self.text[self.index]
                self.index += 1
                return letter
            self.index += 1
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)