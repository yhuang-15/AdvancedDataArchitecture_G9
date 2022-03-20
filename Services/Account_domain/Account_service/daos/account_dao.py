from sqlalchemy import Column, String, Integer, DateTime, Boolean

from db import Base


class AccountDAO(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)  # Auto generated primary key
    account_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email_address = Column(String)
    down_time = Column(DateTime)

    premium_status = Column(Integer) # account priority
    preference = Column(String) # apartment preference (apartment selection critria)
    in_waiting_list = Column(Boolean)  

    has_contract = Column(Boolean)
    bank_account = Column(String)


    def __init__(self, account_id, first_name, last_name, phone_number, email_address, 
                        down_time, premium_status, preference, in_waiting_list, has_contract, bank_account):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.down_time = down_time
        self.premium_status = premium_status
        self.preference = preference
        self.in_waiting_list = in_waiting_list
        self.has_contract = has_contract
        self.bank_account = bank_account

