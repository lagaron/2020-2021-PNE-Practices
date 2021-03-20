from client0 import Client

PRACTICE = 2
EXERCISE = 3

print("-----| Practice {PRACTICE} Exercise {EXERCISE} |-----")

PORT = 6123
IP = "127.0.0.1"
c= Client(IP, PORT)
print("Response: ", c.talk("Hello"))
