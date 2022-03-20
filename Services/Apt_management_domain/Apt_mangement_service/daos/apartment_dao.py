from tkinter.messagebox import NO
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.status_dao import StatusDAO
from constant import STATUS_AVAILABLE
from datetime import datetime
from db import Base


class ApartmentDAO(Base):
    __tablename__ = 'apartment'
    id = Column(Integer, primary_key=True) 
    size = Column(Integer)
    price = Column(Integer)
    status_id = Column(Integer, ForeignKey('status.id'))
    status = relationship(StatusDAO.__name__, backref=backref("apartment", uselist=False))

    def __init__(self, size, price, status = None):
        self.size = size
        self.price = price
        if status is not None:
            self.status = status
        else:
            self.status = StatusDAO(STATUS_AVAILABLE, datetime.now())
