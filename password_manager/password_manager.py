import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from password_manager.base import Base
from password_manager.models import *


class PasswordManager(object):

    def __init__(self, db_filename):
        self._engine = create_engine('sqlite:///' + db_filename)
        if not os.path.isfile(db_filename):
            self._recreate_database()
        self.Session = sessionmaker(self._engine)
        self.session = self.Session()

    def _recreate_database(self):
        Base.metadata.create_all(self._engine)

    def _get_all_objects_of_type(self, type_):
        """
        Request all objects in current database session.

        Arguments:
        type_ -- the class inherited from Base, intended to be a db model
        """
        return self.session.query(type_).all()

    def services(self):
        """
        Get all services in database.
        """
        return self._get_all_objects_of_type(Service)

    def passwords(self):
        """
        Get all passwords in database.
        """
        return self._get_all_objects_of_type(Password)

    def remove_password(self, pk):
        """
        Remove password from database using its primary key.

        Arguments:
        pk -- primary key of object chosen for removal
        """
        self.session.query(Password).filter(Password.password_id==pk).delete()
        self.session.commit()
        self.session.close()

    def remove_service(self, pk):
        """
        Remove service from database using its primary key.

        Arguments:
        pk -- primary key of object chosen for removal
        """
        self.session.query(Service).filter(Service.service_id==pk).delete()
        self.session.commit()
        self.session.close()

    def add_password(self, **kwargs):
        """
        Add new password to database.

        Arguments:
        password_login -- login, associated with password
        password -- password itself
        password_service -- Service object associated with this password
        """
        new_pass = Password(**kwargs)
        self.session.add(new_pass)
        self.session.commit()
        self.session.close()

    def add_service(self, **kwargs):
        """
        Add new service to database.

        Arguments:
        service_name -- name of the service
        """
        new_serv = Service(**kwargs)
        self.session.add(new_serv)
        self.session.commit()
        self.session.close()

