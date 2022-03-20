from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Interval
from sqlalchemy.orm import relationship, backref

from daos.status_dao import StatusDAO
from db import Base


class WaitingListDAO(Base):
    __tablename__ = 'waitingList'
    id = Column(Integer, primary_key=True)  # Auto generated primary key
    application_id = Column(String)
    registration_date = Column(DateTime)
    waiting_time = Column(Interval)
    priority_status = Column(String)
    # reference to status as foreign key relationship. This will be automatically assigned.
    status_id = Column(Integer, ForeignKey('status.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    status = relationship(StatusDAO.__name__, backref=backref("waitingList", uselist=False))

    def __init__(self, application_id, registration_date, waiting_time, priority_status, status):
        self.application_id = application_id
        self.registration_date = registration_date
        self.waiting_time = waiting_time
        self.priority_status = priority_status
        self.status = status
