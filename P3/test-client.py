from client0 import Client

PRACTICE = 3
EXERCISE = 7

print("-----| Practice {PRACTICE} Exercise {EXERCISE} |-----")

PORT = 8080
IP = "127.0.0.1"
c= Client(IP, PORT)
print(c.talk("* Testing GET..."))
print(c.talk(Path("./P2/U5.txt").read_text()))
print(c.talk(Path("U5.txt").read_text()))