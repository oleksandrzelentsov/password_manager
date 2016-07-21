import sqlite3


class Password(object):

    def __init__(self, service_name, login, password):
        self.service_name = service_name
        self.login = login
        self.password = password


class PasswordManager(object):

    def __init__(self, filename='./passdb.sqlite'):
        self.filename = filename
        self.passwords = self._load()

    def add_password(self, password_obj=None, password=None,
                     service=None, login=None):
        if password_obj is None and not all(password, service, login):
            raise Exception('No password data were given to add to database.')
        elif password_obj is not None:
            password = password_obj
        else:
            password = Password(service, login, password)
        self.passwords.append(password)

    def _load(self)
        pass
