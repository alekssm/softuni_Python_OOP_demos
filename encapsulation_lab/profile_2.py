class Profile:
    username_min_length = 5
    username_max_length = 15

    password_min_length = 8
    password_min_upper = 1
    password_min_digit = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, new_username):
        if self.username_min_length > len(new_username) or len(new_username) > self.username_max_length:
            raise ValueError("The username must be between 5 and 15 characters.")

    def __validate_password(self, new_password):
        if len(new_password) < self.password_min_length:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        if len([x for x in new_password if x.isdigit()]) < self.password_min_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        if len([x for x in new_password if x.isupper()]) < self.password_min_upper:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__validate_username(new_username)
        self.__username = new_username

    @property
    def password(self):
        return "".join('*' * len(self.__password))

    @password.setter
    def password(self, value):
        self.__validate_password(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {self.password}'

