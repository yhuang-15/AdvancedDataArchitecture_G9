import datetime

from constant import STATUS_CREATED
from daos.application_dao import ApplicationDAO
from daos.status_dao import StatusDAO
from db import Session, engine, Base

# os.environ['DB_URL'] = 'sqlite:///delivery.db'
# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()


status_1 = StatusDAO(STATUS_CREATED, datetime.datetime.now())
application_1 = ApplicationDAO("cus_1", "appl_1", "apartment_1", datetime.datetime.now(),
                         status_1)

session.add(status_1)
session.add(application_1)

# 10 - commit and close session
session.commit()
session.close()
