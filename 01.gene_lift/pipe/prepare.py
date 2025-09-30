fi = open('gene.list')
fo = open('run01.sh', 'w')
for line in fi:
    geneID = line.rstrip('\n')
    fo.write(f'blastn -task blastn -query ../source/gene/{geneID}.gene.fa -db ../target/blastDB/ref.fa -dust no -soft_masking false -word_size 28 -perc_identity 80 -qcov_hsp_perc 20 -outfmt 6 -out blastn/{geneID}.blastn\n')
fo.close()
