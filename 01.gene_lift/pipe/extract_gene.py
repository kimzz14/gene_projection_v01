from Bio.Seq import Seq
import pysam

fasta = pysam.FastaFile("../target/ref.fa")

fi = open('passed.gene.map')

legend_LIST = ['geneID', 'chrom', 'strand', 'query_sPos', 'query_ePos', 'sbjct_sPos', 'sbjct_ePos', 'coverage', 'identity', 'hspN']

geneN = 0
for line in fi:
    data_LIST = line.rstrip('\n').split('\t')
    if len(legend_LIST) != len(data_LIST): continue
    fields = {key:value for key, value in zip(legend_LIST, data_LIST)}

    geneID = fields['geneID']
    chrom = fields['chrom']
    strand = fields['strand']
    sPos = int(fields['sbjct_sPos'])
    ePos = int(fields['sbjct_ePos'])

    sequence = fasta.fetch(chrom, sPos, ePos)
    if strand == '-':
        sequence = str(Seq(sequence).reverse_complement())

    fo = open(f'gene/{geneID}.gene.fa', 'w')
    fo.write(f'>{geneID}:{chrom}:{strand}:{sPos}:{ePos}\n')
    fo.write(sequence + '\n')
    fo.close()
    geneN += 1

print(geneN)
