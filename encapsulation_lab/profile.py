class Profile:
    def __init__(self, username, password):
        self.__set_username(username)
        self.__set_password(password)

    def __set_username(self, new_username):
        if 5 > len(new_username) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = new_username

    def __set_password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        if not any([x for x in new_password if x.isdigit()]):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        if not any([x for x in new_password if x.isupper()]):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = new_password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def __str__(self):
        return f'You have a profile with username: "{self.get_username()}" and password: {"*" * len(self.get_password())}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)