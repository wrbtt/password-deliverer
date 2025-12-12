import secrets
import string


class Password:

    def __init__(self):
        self.password_storage = []

    def generation_password(string_length):
        characters = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(characters) for _ in range(string_length))

        return password
    
    def container_for_password(self, count=1, length=12):
        for _ in range(count):
            item = self.generation_password(length)
            self.password_storage.append(item)

        return self.password_storage
    
    def get_storage(self):
        return self.password_storage
    
    def clear_storage(self):
        self.password_storage = []