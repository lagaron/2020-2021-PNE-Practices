from client0 import Client

PRACTICE = 2
EXERCISE = 3

print("-----| Practice {PRACTICE} Exercise {EXERCISE} |-----")

PORT = 6123
IP = "127.0.0.1"
c= Client(IP, PORT)

s= Seq()
s.seq_read_fasta('../Session-04/FRAT!.txt')

#for i in range(0, len(s.strbases), 10):
    #fragment = s.strbases[i:i+10]
    #if count == 5:
        #break

count = 0
i= 0
while i < len(s.strbases) and count <5:
    fragment = s.strbases[i:i+10]
    count +=1
    i+=10
    print("Fragment", count, ":", fragment)
    print(c.talk(fragment))