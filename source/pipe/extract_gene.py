from Bio.Seq import Seq
import pysam

fasta = pysam.FastaFile("ref.fa")

fi = open('gene.gff3')
fo_fa = open('gene.fa', 'w')
fo_list = open('gene.list', 'w')
geneN = 0
for line in fi:
    if line.startswith('#') == True: continue
    data_LIST = line.rstrip('\n').split('\t')
    if len(data_LIST) != 9:
        continue

    chrom, source, feature, sPos, ePos, score, strand, _, description = data_LIST

    if feature != 'gene': continue
    #print(chrom, source, type1, sPos, ePos, score, strand, _, description)

    sPos = int(sPos)
    ePos = int(ePos)
    geneID = description.split(';')[0].split('=')[1]

    sequence = fasta.fetch(chrom, sPos, ePos)
    if strand == '-':
        sequence = str(Seq(sequence).reverse_complement())


    fo_list.write(geneID + '\n')

    fo_fa.write(f'>{geneID}:{chrom}:{strand}:{sPos}:{ePos}\n')
    fo_fa.write(sequence + '\n')

    fo = open(f'gene/{geneID}.gene.fa', 'w')
    fo.write(f'>{geneID}:{chrom}:{strand}:{sPos}:{ePos}\n')
    fo.write(sequence + '\n')
    fo.close()
    geneN += 1

print(geneN)

fo_list.close()
fo_fa.close()
fi.close()
