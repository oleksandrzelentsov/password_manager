import os
import random
import myModule
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from password_manager.base import Base
from password_manager.models import *


schema_path = './schema.sql'


class PasswordManager(object):

    def __init__(self, db_filename):
        self.engine = create_engine('sqlite:///' + db_filename)
        if not os.path.isfile(db_filename):
            print 'created database in {}'.format(db_filename)
            self._recreate_database()
        self.session = sessionmaker(self.engine)

    def _recreate_database(self):
        Base.metadata.create_all(self.engine)

    def _generate_password(self, length):
        return myModule.generate_password(length, random.randrange(100))

    def _get_all_objects_of_type(self, type_):
        return self.session().query(type_).all()

    def services(self):
        return self._get_all_objects_of_type(Service)

    def passwords(self):
        return self._get_all_objects_of_type(Password)

    def remove_password(self, pk):
        s = self.session()
        s.query(Password).filter(Password.password_id==pk).delete()
        s.commit()
        return 0

    def remove_service(self, pk):
        s = self.session()
        s.query(Service).filter(Service.service_id==pk).delete()
        s.commit()
        return 0

    def add_password(self, **kwargs):
        new_pass = Password(**kwargs)
        s = self.session()
        s.add(new_pass)
        s.commit()

    def add_service(self, **kwargs):
        new_serv = Service(**kwargs)
        s = self.session()
        s.add(new_serv)
        s.commit()


if __name__ == '__main__':
    PasswordManager('./db.sqlite')

