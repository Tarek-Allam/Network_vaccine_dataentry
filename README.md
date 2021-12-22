# Server-Client  vaccine data entry

final project of computer networking class.

**Team Members**

* Tarek Allam Ibrahim section: 1 BN: 42
* Mahmoud mohammed Tarek section:    BN:
* Mahmoud mohammed ibrahim section:  BN:
* Abd alrahman abu bakr section:  BN:
* hedra sami section:  BN:

### screen shoots from Application user interface

### Intiate connection with three-way hand-shake

![intiate connection](resources/hand-shake.png)

### intiate connection

![Home Page Search for a record ](resources/Landing-page.png)

### Home Page

![New record](resources/create-record.png)

### New record

![View saved record ](resources/record-added.png)

### View saved record

![New connection accepted](resources/multi-tcp-conection.png)

### multi-tcp-conections

![multi-tcp-conection](resources/multi-tcp-conection.png)

### chat loop deals with the database, socket states, while the connections in sessions

![Server History log](resources/all-server-logs.png)

## extra feature added and methods

1. socket programming (TCP)
2. Handlling MultiClient Server Communication
3. sqllite3 for database management
4. simple graphical user interface for the data record

## how to use

First make sure you have requirements `pip install -r requirements.txt`

The client runs the server code in terminal  `python server.py`
then run the client code `python client.py`

## Sequence of Sockets Communication

![Sockets communication diagram](resources/Socket_server.png)