import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import jinja2
import pathlib
import json
import server_utils as su

genes_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested:", path_name)
        print("Parameters:", arguments)
        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        SERVER = "rest.ensembl.org"
        PARAMS = "?content-type=application/json"
        connection = http.client.HTTPConnection(SERVER)

        context = {}

        if path_name == "/":
            contents = read_template_html_file("./html/index.html").render(context=context)
        elif path_name.split('?')[0] == "/listSpecies":
            try:
                ENDPOINT = "/info/species/"
                connection.request("GET", ENDPOINT + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                species_list = []
                for n in range(0, int(arguments["limit"][0])):
                    species_list.append(response_dict['species'][n]['common_name'])

                context = {"number_seq": len(response_dict["species"]),
                           "number_limit": arguments["limit"][0],
                           "list_species": species_list}


                contents = read_template_html_file("./html/listSpecies.html").render(context=context)

            except ValueError:

                contents = read_template_html_file("./html/error.html").render(context=context)

            except IndexError:

                contents = read_template_html_file("./html/error.html").render(context=context)

        elif path_name.split('?')[0] == "/karyotype":
            try:
                ENDPOINT = "/info/assembly/"
                species = arguments["species"][0]
                connection.request("GET", ENDPOINT + species + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                karyotype_list = []
                for n in response_dict["karyotype"]:
                    karyotype_list.append(n)

                context = {"specie": species,
                           "karyotype": karyotype_list}

                contents = read_template_html_file("./html/karyotype.html").render(context=context)

            except ValueError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except UnboundLocalError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except KeyError:
                contents = read_template_html_file("./html/error.html").render(context=context)

        elif path_name.split('?')[0] == "/chromosomeLength":
            try:
                ENDPOINT = "/info/assembly/"
                species = arguments["species"][0]
                chromosome = arguments["chromosome"][0]
                connection.request("GET", ENDPOINT + species + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())

                for n in range(0, len(response_dict["top_level_region"])):
                    if response_dict["top_level_region"][n]["name"] == chromosome:
                        chromosome_length = response_dict["top_level_region"][n]["length"]
                        context = {"chromosome_length": chromosome_length}
                    else:
                        pass
                if context:
                    contents = read_template_html_file("./html/chromosomeLength.html").render(context=context)
                else:
                    contents = read_template_html_file("./html/error.html").render(context=context)

            except ValueError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except UnboundLocalError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except KeyError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except IndexError:
                contents = read_template_html_file("./html/error.html").render(context=context)


        elif path_name.split('?')[0] == "/geneSeq":
            try:
                ENDPOINT = "/sequence/id/"
                gene = arguments["gene"][0]
                gene_id = genes_dict[gene]
                connection.request("GET", ENDPOINT + gene_id + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())

                context = {"gene": gene,
                           "sequence": response_dict["seq"]}
                contents = read_template_html_file("./html/geneSeq.html").render(context=context)

            except ValueError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except UnboundLocalError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except KeyError:
                contents = read_template_html_file("./html/error.html").render(context=context)

        elif path_name.split('?')[0] == "/geneInfo":
            try:
                ENDPOINT = "/sequence/id/"
                gene = arguments["gene"][0]
                gene_id = genes_dict[gene]
                connection.request("GET", ENDPOINT + gene_id + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())

                context = {"gene": gene,
                           "start": response_dict["desc"].split(":")[3],
                           "end": response_dict["desc"].split(":")[4],
                           "length": str(int(response_dict["desc"].split(":")[4])-int(response_dict["desc"].split(":")[3])),
                           "id": gene_id,
                           "chromosome_name": response_dict["desc"].split(":")[1]
                           }

                contents = read_template_html_file("./html/geneInfo.html").render(context=context)

            except ValueError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except UnboundLocalError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except KeyError:
                contents = read_template_html_file("./html/error.html").render(context=context)

        elif path_name.split('?')[0] == "/geneCalc":
            try:
                ENDPOINT = "/sequence/id/"
                gene = arguments["gene"][0]
                gene_id = genes_dict[gene]
                connection.request("GET", ENDPOINT + gene_id + PARAMS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                sequence = response_dict["seq"]
                seq1 = su.Seq(sequence)
                context = {"gene": gene_id,
                           "count_bases": seq1.count_bases()[0],
                           "percentage": seq1.count_bases()[1]}

                contents = read_template_html_file("./html/geneCalc.html").render(context=context)

            except ValueError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except UnboundLocalError:
                contents = read_template_html_file("./html/error.html").render(context=context)
            except KeyError:
                contents = read_template_html_file("./html/error.html").render(context=context)

        else:
            contents = read_template_html_file("./html/error.html").render(context=context)

        # Message to send back to the clinet

        # Generating the response message
        # -- Status line: OK!
        self.send_response(200)
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()