class User:
    def __init__(self, firstname: str, lastname: str, fav_animal: str, zodiac_sign: str):
        self.firstname = firstname
        self.lastname = lastname
        self.fav_animal = fav_animal
        self.zodiac_sign = zodiac_sign


test_user = User("Иван", "Смирнов", "Лиса", "Водолей")


def get_wish(user: User) -> str:
    wish_template = '''Индивидуальный гороскоп для пользователя %s %s
Кем вы были в прошлой жизни: %s
Ваш знак зодиака - %s , поэтому вы - тонко чувствующая натура.'''
    return wish_template % (user.firstname, user.lastname, user.fav_animal, user.zodiac_sign)


print(get_wish(test_user))
