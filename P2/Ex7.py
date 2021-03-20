from client0 import Client

PRACTICE = 2
EXERCISE = 3

print("-----| Practice {PRACTICE} Exercise {EXERCISE} |-----")

PORT = 6123
PORT2 = 12300
IP = "127.0.0.1"
c = Client(IP, PORT)
c_2= Client(IP, PORT2)

s = Seq()
s.seq_read_fasta('../Session-04/FRAT!.txt')

count = 0
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i:i + 10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    if count % 2 == 0:
        print(c_2.talk("Fragment", str(count), ":", fragment))
    else:
        print(c.talk("Fragment", str(count), ":", fragment))

