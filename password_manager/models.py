from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from password_manager.base import Base


class Service(Base):
    __tablename__ = 'services'

    service_id = Column(Integer, primary_key=True)
    service_name = Column(String(64))

    def __repr__(self):
        return "Service(service_id={}, service_name='{}')".format(self.service_id, self.service_name)

    def __str__(self):
        return self.__repr__()


class Password(Base):
    __tablename__ = 'passwords'

    password_id = Column(Integer, primary_key=True)
    password_service_id = Column(Integer(), ForeignKey('services.service_id'))
    password_login = Column(String(32))
    password = Column(String(256))

    def __repr__(self):
        return "Password(password_id={}, password_login='{}', password='{}', password_service={})".format(self.password_id, self.password_login, self.password, str(self.password_service))

    def __str__(self):
        return self.__repr__()

    password_service = relationship('Service', backref=backref('passwords'), lazy='joined')

