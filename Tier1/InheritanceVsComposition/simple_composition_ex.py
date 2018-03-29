#!/usr/bin/env python3

class User(object):
    def __init__(self, name, lastname, details):
        self.name = name
        self.lastname = lastname
        self.details = details


class UserDetails(object):
    def __init__(self, email, ci_number):
        self.email = email
        self.ci_number = ci_number


if __name__ == '__main__':
    details = UserDetails('cm@cm.com', '1725651630')
    user = User('Cristhian', 'Motoche', details)
    # Se accede a los atributos (y métodos) del objeto compuesto
    print(user.name)
    print(user.details.email)
