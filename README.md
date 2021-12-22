# Server-Client  vaccine data entry

final project of computer networking class.

**Team Members**
| name | section | BN |   
|------------------------|---------|----| | Tarek ALlam Ibrahim | 2 | 42 | | Mahmoud mohammed Tarek | | | | Mahmoud
mohammed ibrahim | | | | Abd alrahman abu bakr | | | | hedra sami | | |

### screen shoots from Application user interface

![intiate connection](resources/hand-shake.png)
![Home Page](resources/Landing-page.png)
![New record](resources/create-record.png)
![View saved record ](resources/record-added.png)
![New connection accepted](resources/multi-tcp-conection.png)
![database record ](resources/multi-tcp-conection.png)

### chatLoop deals with the database, socket states, while the connections in sessions

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