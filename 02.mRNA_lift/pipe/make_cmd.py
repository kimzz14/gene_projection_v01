feature = 'mrna'

gene_DICT = {}
fi = open('../01.gene_lift/gene.map')
for line in fi:
    gene_id = line.rstrip('\n').split('\t')[0]
    gene_DICT[gene_id] = {}
fi.close()

fi = open('../source/gene2mrna')

mrna_DICT = {}

for line in fi:
    gene_id, mrna_id = line.rstrip('\n').split('\t')
    if gene_id in gene_DICT: 
        mrna_DICT[mrna_id] = gene_id
fi.close()

fo = open('run01.sh', 'w')
fi = open(f'../source/{feature}.list')
for line in fi:
    mrna_id = line.rstrip('\n')
    gene_id = mrna_DICT[mrna_id]

    if gene_id in gene_DICT:
        fo.write(f'bash pipe/pipe_exonerate.sh {gene_id} {mrna_id}\n')
fi.close()

fo.close()