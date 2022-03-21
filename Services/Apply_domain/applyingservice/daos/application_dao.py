from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.status_dao import StatusDAO
from db import Base


class ApplicationDAO(Base):
    __tablename__ = 'application'
    application_id = Column(Integer, primary_key=True)  # Auto generated primary key
    user_id = Column(String)
    apartment_id = Column(String)
    application_time = Column(DateTime)
    # reference to status as foreign key relationship. This will be automatically assigned.
    status_id = Column(Integer, ForeignKey('status.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    status = relationship(StatusDAO.__name__, backref=backref("application", uselist=False))

    def __init__(self, application_id, user_id, apartment_id, application_time, status):
        self.application_id = application_id
        self.user_id = user_id
        self.apartment_id = apartment_id
        self.application_time = application_time
        self.status = status
