class User:
    def __init__(self, user_id, name, access_level='user'):
        self.user_id = user_id
        self.name = name
        self._access_level = access_level

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.users = []

    def add_user(self, user):
        if isinstance(user, User) and user not in self.users:
            self.users.append(user)

    def remove_user(self, user_id):
        self.users = [user for user in self.users
                      if user.user_id != user_id]

    def list_users(self):
        for user in self.users:
            print(f'ID: {user.user_id}, Name: {user.get_name()}, 'f'Access Level: {user.get_access_level()}')

# Пример использования
admin = Admin('001', 'Admin User')
user1 = User('002', 'John Doe')
user2 = User('003', 'Jane Doe')

admin.add_user(user1)
admin.add_user(user2)

print("Перед удалением:")
admin.list_users()

admin.remove_user('002')

print("\nПосле удаления пользователя с ID '002':")
admin.list_users()
