fi = open('gene.gff3')
fo = open('gene2mrna', 'w')

gene_DICT = {}

for line in fi:
    if line.startswith('#') == True: continue
    data_LIST = line.rstrip('\n').split('\t')
    if len(data_LIST) != 9:
        continue

    chrom, source, feature, sPos, ePos, score, strand, _, description = data_LIST

    if feature != 'mRNA': continue

    fields = {}
    for item in description.split(';'):
        if len(item.split('=')) != 2: continue
        key, value = item.split('=')
        fields[key] = value

    mRNA_ID = fields['ID']
    gene_ID = fields['Parent']
    fo.write(gene_ID + '\t' + mRNA_ID + '\n')
fo.close()
