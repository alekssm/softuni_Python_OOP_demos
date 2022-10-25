class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.id = id
        self.balance = balance
        self.pin = pin

    def __right_pin(self, pin):
        return self.pin == pin

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        self.__balance = value

    def get_id(self, pin):
        if not self.__right_pin(pin):
            return "Wrong pin"
        return self.id

    def change_pin(self, old_pin, new_pin):
        if not self.__right_pin(old_pin):
            return "Wrong pin"
        self.pin = new_pin
        return "Pin changed"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))