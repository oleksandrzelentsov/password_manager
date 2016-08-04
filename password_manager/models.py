from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Base


class Service(Base):
    __tablename__ = 'services'

    service_id = Column(Integer, primary_key=True)
    service_name = Column(String(64))

    def __repr__(self):
        return "Service(service_name='{}')".format(self.service_name)


class Password(Base):
    __tablename__ = 'passwords'

    password_id = Column(Integer, primary_key=True)
    service_id = Column(Integer(), ForeignKey('services.service_id'))
    password_login = Column(String(32))
    password = Column(String(256))

    def __repr__(self):
        return "Password(password_login='{}', password='{}')".format(self.password_login, '*'*len(self.password))

    service = relationship('Service', backref=backref('passwords'))
