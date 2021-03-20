from client0 import Client

PRACTICE = 2
EXERCISE = 3

print("-----| Practice {PRACTICE} Exercise {EXERCISE} |-----")

PORT = 6123
IP = "127.0.0.1"
c= Client(IP, PORT)
print(c.talk("Sending the U5 Gene to the server..."))
print(c.talk(Path("./P2/U5.txt").read_text()))     #We dont have this U5 so no working :/
print(c.talk(Path("U5.txt").read_text()))