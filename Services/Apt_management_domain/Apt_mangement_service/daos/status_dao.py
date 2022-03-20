from asyncio.windows_events import NULL
from sqlalchemy import Column, String, Integer, TIMESTAMP, DateTime

from db import Base


class StatusDAO(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True) # Auto generated primary key
    status = Column(String)
    start_date = Column(String, nullable=True)
    end_date = Column(String, nullable = True)
    last_update = Column(TIMESTAMP(timezone=False))

    def __init__(self, status, last_update, start_date = None, end_date = None):
        self.status = status
        self.last_update = last_update
        
        self.start_date = start_date
        self.end_date = end_date
