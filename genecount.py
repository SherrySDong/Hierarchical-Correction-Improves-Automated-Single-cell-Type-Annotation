import glob

genecount = {}
allgenes = open('genes.txt', 'w')
all_data = glob.glob('../processed/*_0.csv')
for data in all_data:
    the_file = open(data, 'r')
    print(data)
    line = the_file.readline()
    line=line.strip() 
    table = line.split('\t')
    table.pop(0)
    for gene in table:
        if gene in genecount:
            genecount[gene] = genecount[gene]  + 1
        else:
            genecount[gene] = 1

all_genes = genecount.keys()
for gene in all_genes:
    allgenes.write(gene)
    allgenes.write('\t')
    allgenes.write(str(genecount[gene]))
    allgenes.write('\n')
