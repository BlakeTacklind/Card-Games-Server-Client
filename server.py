from cardMethods import *
import socket

myPort = 11337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', myPort))
s.listen(5)
