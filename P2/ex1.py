from client0 import Client

PRACTICE = 2
EXERCISE = 1

print("-----| Practice {PRACTICE} Exercise {EXERCISE} |-----")

PORT = 6123
IP = "127.0.0.1"
C= Client(IP, PORT)
C.advanced_ping()
