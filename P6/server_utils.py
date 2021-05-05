from Seq1 import Seq
from jinja2 import Template
import pathlib

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip = "False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping():
    print_colored("PING command!", "green")

def seq_info (sequence):
    object = Seq(sequence)
    variable = object.count_bases()
    lenght = object.len()
    p_one= (variable[0]*100)/ lenght
    p_two = (variable[1] * 100) / lenght
    p_three = (variable[2] * 100) / lenght
    p_four = (variable[3] * 100) / lenght
    response = "Sequences: " + sequence + "\n" + "Total length: " + str(lenght) + "\n" +"A: " + str(variable[0]) +" (" + str(p_one) + "%)" + "\n" + "C: " + str(variable[1]) +" (" + str(p_two) + "%)" + "\n" + "G: " + str(variable[2]) +" (" + str(p_three) + "%)" + "\n" + "T: " + str(variable[3]) +" (" + str(p_four) + "%)" + "\n"
    context = {
        "sequence": sequence,
        "info": response
    }
    contents = read_template_html_file("./html/info.html").render(context=context)
    return contents

def seq_comp (sequence):
    object = Seq(sequence)
    variable = object.complementary()
    context = {
        "sequence": sequence,
        "comp": variable
    }
    contents = read_template_html_file("./html/comp.html").render(context=context)
    return contents


def seq_rev(sequence):
    object = Seq(sequence)
    variable = object.reverse()
    context = {
        "sequence": sequence,
        "rev": variable
    }
    contents = read_template_html_file("./html/rev.html").render(context=context)
    return contents

def seq_gene(cs, Seq, argument):
    location = "./Sequences/"
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

def get(LIST_SEQUENCES, number_sequence):
    context = {
        "number": number_sequence,
        "sequence": LIST_SEQUENCES[int(number_sequence)]

    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

def gene(seq_name):
    PATH = "./Sequences/" + seq_name + ".txt"
    s1= Seq()
    s1.read_fasta(PATH)
    context = {
        "gene_name": seq_name,
        "gene_contents": s1.str_bases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents

#U5.def operation():
