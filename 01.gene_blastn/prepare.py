fi = open('gene.list')

for line in fi:
    geneID = line.rstrip('\n')
    print(f'blastn -task blastn -query ../db/wheat.CS.Gapless/gene/{geneID}.gene.fa -db ../db/Keumkang_v1.0.0/blastDB/ref.fa -dust no -soft_masking false -word_size 28 -perc_identity 80 -qcov_hsp_perc 20 -outfmt 6 -out result/{geneID}.blastn')
