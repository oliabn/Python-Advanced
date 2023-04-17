"""class  User:
Клас користувача, що містить у собі такі методи:
- get_full_name (ПІБ з поділом через пробіл: «Петров Ігор Сергійович»),
- get_short_name (формату ПІБ: «Петров І. С.»),
- get_age (повертає вік користувача, використовуючи поле birthday типу datetime.date);
- метод __str__ (повертає ПІБ та дату народження);
"""

from datetime import date
# from typing import Optional
from email_password import EMAIL


class User:
    def __init__(self,
                 full_name: str,
                 short_name: str,
                 birthday: date,        # date(year, month, day)
                 email: str) -> None:

        self.full_name = full_name
        self.short_name = short_name
        self.birthday = birthday
        self.email = email

    def __str__(self) -> str:
        return f'Full name: {self.full_name}, birthday: {self.birthday}'

    def get_full_name(self) -> str:
        return self.full_name

    def get_short_name(self) -> str:
        return self.short_name

    def get_age(self) -> int:
        today = date.today()
        age = (today.year - self.birthday.year -
               ((today.month, today.day) < (self.birthday.month, self.birthday.day)))
        return age


# Test
if __name__ == '__main__':

    user = User(full_name='Petrenko Igor Sergijovych',
                short_name='Petrenko I. S.',
                birthday=date(1991, 2, 4),
                email=EMAIL)
    print(user)
    print(f'Age: {user.get_age()}')
