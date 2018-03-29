#!/usr/bin/env python3

class User(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class UserDetails(User):
    def __init__(self, name, lastname, email, ci_number):
        User.__init__(self, name, lastname)
        self.email = email
        self.ci_number = ci_number


if __name__ == '__main__':
    details = UserDetails('Cristhian', 'Motoche', 'cm@cm.com', '1725651630')
    # Se sobrescriben los atributos (y métodos)
    print(details.name)
    print(details.email)
