query = 'wheat.CS.Gapless'


mRNA_DICT = {}
fi = open('gene.list')
for line in fi:
    gene_id = line.rstrip('\n').split('\t')[0]
    mRNA_DICT[gene_id] = []
fi.close()

fi = open(f'../db/{query}/cds.list')
for line in fi:
    mRNA_id = line.rstrip('\n')
    gene_id = '.'.join(mRNA_id.split('.')[:-1])

    if gene_id in mRNA_DICT:
        print(f'bash pipe_exonerate.sh {gene_id} {mRNA_id}')
fi.close()

