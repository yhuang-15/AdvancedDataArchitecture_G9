This sub-domain contains two services:

    - account service handles the operations on the user accounts
    
    - notification service handles sending the notification to users via email when there's any changes to their accounts.

|      account_service    |          POST          |       GET       |       PUT      |      DELETE     |
|:-----------------------:|:----------------------:|:---------------:|:--------------:|:---------------:|
|       /accounts         | create new account     |  list all accs  |       405      | delete all accs |
|     /accounts/<a_id>    |           405          | get acc details | update details |    delete apt   |


|      notify _service    |          POST          |       GET       |       PUT      |      DELETE     |
|:-----------------------:|:----------------------:|:---------------:|:--------------:|:---------------:|
|       /auto_notifiy     |   send notification    |       405       |       405      |        405      |

