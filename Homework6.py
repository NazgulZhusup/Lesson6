# Разработай систему управления учетными записями пользователей для небольшой компани
# и. Компания разделяет сотрудников на обычных работников и администраторов. У каждого
# сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы,
# помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять
# или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень
# доступа ('user' для обычных сотрудников).
#
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный
# атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также
# содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей
# из списка (представь, что это просто список экземпляров `User`).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации
# снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

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
        self.users.append(user)

    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]

    def list_users(self):
        for user in self.users:
            print(f'ID: {user.user_id}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')


admin = Admin('001', 'Admin User')
user1 = User('002', 'John Doe')
user2 = User('003', 'Jane Doe')
admin.add_user(user1)
admin.add_user(user2)

admin.list_users()
admin.remove_user('002')
print("\nAfter removing John Doe:")
admin.list_users()






