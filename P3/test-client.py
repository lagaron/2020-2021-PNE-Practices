from client0 import Client

PRACTICE = 3
EXERCISE = 7

print("-----| Practice {PRACTICE} Exercise {EXERCISE} |-----")

PORT = 8080
IP = "127.0.0.1"
c= Client(IP, PORT)
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