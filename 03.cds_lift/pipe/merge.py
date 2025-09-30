feature = 'cds'

gene_DICT = {}
fi = open('../01.gene_lift/passed.gene.map')
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

fo_gff3 = open(f'{feature}.gff3', 'w')
fi = open(f'../source/{feature}.list')
for line in fi:
    mrna_id = line.rstrip('\n')
    if not mrna_id in mrna_DICT: continue

    fi_gff3 = open(f'gff3/{mrna_id}.{feature}.gff3')

    for line in fi_gff3:
        fo_gff3.write(line)
    fi_gff3.close()
    
fi.close()

fo_gff3.close()