# 1 - imports
from daos.application_dao import ApplicationDAO
from db import Session

# 2 - extract a session
session = Session()

applications = session.query(ApplicationDAO).all()

# 4 - print deliveries' details
print('\n### All deliveries:')
for application in applications:
    print(f'{application.apartment_id} was created by {application.user_id}. Its current status is {application.status.status}')
print('')
