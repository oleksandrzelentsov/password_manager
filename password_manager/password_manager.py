import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import myModule

from base import Base
from models import *


class PasswordManager(object):

    def __init__(self, db_filename):
        self._engine = create_engine('sqlite:///' + db_filename)
        if not os.path.isfile(db_filename):
            self._recreate_database()
        self.Session = sessionmaker(self._engine)
        self.session = self.Session()

    def _recreate_database(self):
        Base.metadata.create_all(self._engine)

    def _generate_password(self, length):
        return myModule.generate_password(length, random.randrange(100))

    def _get_all_objects_of_type(self, type_):
        return self.session.query(type_).all()

    def services(self, session=None):
        return self._get_all_objects_of_type(Service)

    def passwords(self, session=None):
        return self._get_all_objects_of_type(Password)

    def remove_password(self, pk):
        self.session.query(Password).filter(Password.password_id==pk).delete()
        self.session.commit()
        self.session.close()

    def remove_service(self, pk):
        self.session.query(Service).filter(Service.service_id==pk).delete()
        self.session.commit()
        self.session.close()

    def add_password(self, **kwargs):
        new_pass = Password(**kwargs)
        self.session.add(new_pass)
        self.session.commit()
        self.session.close()

    def add_service(self, **kwargs):
        new_serv = Service(**kwargs)
        self.session.add(new_serv)
        self.session.commit()
        self.session.close()

