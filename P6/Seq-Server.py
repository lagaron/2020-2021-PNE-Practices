import socket
import server_utils
from Seq1 import Seq

list_sequences =["ACGTTTACTGCTAGTTACCCCT", "AGTCCCCTGGGTACTTTTACC", "GTTTTACTTTTAAAAGTCCCA", "AAAATTTTCCCGGGTGTGACCCAT", "AGGGGAATTTTTCGGGATCCCATAAAT"]
ls= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT= 8080
IP= "127.0.0.1"

ls= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
count_connections= 0
ls.listen()

print("The server is configured!")
client_address_list=[]
while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port)= ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + "CLIENT IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    msg_raw = cs.recv(2048)
    msg= msg_raw.decode()

    formatted_message = server_utils.format_command(msg)
    formatted_message= formatted_message.split(" ")

    if len(formatted_message) == 1:
        command = formatted_message[0]

    else:
        command= formatted_message[0]
        argument = formatted_message[1]

    if command == "PING":
        server_utils.ping()
        response = "OK!"
        cs.send(str(response).encode())

    elif command == "GET":
        server_utils.print_colored("GET", "yellow")
        response = list_sequences[int(argument)]
        print(response)
        cs.send(response.encode())

    elif command == "INFO":
        server_utils.info_color()
        server_utils.seq_info(cs, Seq, argument)


    elif command == "COMP":
        server_utils.comp_color()
        server_utils.seq_comp(cs, Seq, argument)


    elif command == "REV":
        server_utils.rev_color()
        server_utils.seq_rev(cs, Seq, argument)

    elif command == "GENE":
        server_utils.gene_color()
        server_utils.seq_gene(cs, Seq, argument)

    else:
        response = "Not available command"
        cs.send(str(response).encode())
    cs.close()
