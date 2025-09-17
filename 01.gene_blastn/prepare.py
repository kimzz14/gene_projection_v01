fi = open('gene.list')

for line in fi:
    geneID = line.rstrip('\n')
    print(f'blastn -task blastn -query ../db/CS.Gapless/gene/{geneID}.gene.fa -db ../db/Keumkang_v1.0.0/blastDB/ref.fa -dust no -soft_masking false  -outfmt 6 -out {geneID}.blastn')