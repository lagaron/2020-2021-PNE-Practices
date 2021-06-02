import P0.Seq0 as Seq0
gene_folder = "./Sequences/"
gene_list = ["U5", "ADA", "PRAT1", "FXN"]


print("-----| Exercise 5 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(gene_folder + gene + ".txt")
    print("Gene ", gene, ":", Seq0.seq_count(sequence))