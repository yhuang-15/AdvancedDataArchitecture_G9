# Apartment management  service

The aim is here to be able to create and manage apartments in the company, with the attributes being 'size', 'price', and 'status'.  

  Below you'll find an explanation to the API methods.

|                         |          POST          |       GET       |       PUT      |      DELETE     |
|:-----------------------:|:----------------------:|:---------------:|:--------------:|:---------------:|
|       /apartments       | create new aptinstance |  list all apts  |       405      | delete all apts |
|     /apartments/apt1    |           405          | get apt details | update details |    delete apt   |
| /apartments/apt1/status |           405          |    get status   |  update status |       405       |