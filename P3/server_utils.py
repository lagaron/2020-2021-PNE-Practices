
def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip = "False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping():
    print_colored("PING command!", "green")

def seq_info (cs,Seq, argument):
    object = Seq(argument)
    variable = object.count_bases()
    lenght = object.len()
    p_one= (variable[0]*100)/ lenght
    p_two = (variable[1] * 100) / lenght
    p_three = (variable[2] * 100) / lenght
    p_four = (variable[3] * 100) / lenght
    response = "Sequence: " + argument + "\n" + "Total length: " + str(lenght) + "\n" +"A: " + str(variable[0]) +" (" + str(p_one) + "%)" + "\n" + "C: " + str(variable[1]) +" (" + str(p_two) + "%)" + "\n" + "G: " + str(variable[2]) +" (" + str(p_three) + "%)" + "\n" + "T: " + str(variable[3]) +" (" + str(p_four) + "%)" + "\n"
    print(response)
    cs.send(response.encode())

def seq_comp(cs, Seq, argument):
    object = Seq(argument)
    variable = object.complementary() + "\n"
    print(variable)
    cs.send(variable.encode())

def seq_rev(cs, Seq, argument):
    object= Seq(argument)
    variable = object.reverse() + "\n"
    print(variable)
    cs.send(variable.encode())

def seq_gene(cs, Seq, argument):
    location = "./Sequence/"
    object = Seq(argument)
    object.read_fasta(location + argument)
    response = str(object)
    print(response)
    cs.send(response.encode())

def info_color ():
    print_colored("INFO", "green")

def comp_color():
    print_colored("COMP", "green")

def rev_color():
    print_colored("REV", "green")

def gene_color():
    print_colored("GENE", "green")