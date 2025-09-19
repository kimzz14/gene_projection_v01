import sys

cdsID = sys.argv[1]

fi = open(f'gff2/{cdsID}.gff2')
fo = open(f'gff3/{cdsID}.gff3', 'w')
exonN = 0
isFirst = True

for line in fi:
    if line.startswith('Command') == True: continue
    if line.startswith('Hostname') == True: continue
    if line.startswith('vulgar') == True: continue
    if line.startswith('#') == True: continue
    data_LIST = line.rstrip('\n').split('\t')
    if len(data_LIST) != 9: continue
    seqName, source, feature, start, end, score, strand, frame, attribute = data_LIST
    start = int(start)
    end = int(end)

    geneID, gene_chrom, gene_strand, gene_sPos, gene_ePos = seqName.split(':')

    if isFirst == True:
        fo.write('\t'.join(map(str, [gene_chrom, source, 'gene', gene_sPos, gene_ePos, '.', gene_strand, frame, f'ID={geneID}'])) + '\n')
        isFirst = False


    gene_sPos = int(gene_sPos)
    gene_ePos = int(gene_ePos)

    if feature == 'utr5': continue
    if feature == 'utr3': continue
    if feature == 'splice5': continue
    if feature == 'splice3': continue
    if feature == 'intron': continue
    if feature == 'similarity': continue

    if feature == 'gene':
        description = f'ID={cdsID};Parent={geneID}'

        adjust_feature = 'mRNA'
    if feature == 'exon':
        adjust_feature = 'exon'
        exonN += 1
        #description = f'ID={geneID}.{exonN};Parent={geneID}'
        description = f'Parent={cdsID}'

    if gene_strand == '+':
        adjust_sPos = gene_sPos - 1 + start
        adjust_ePos = gene_sPos - 1 + end
    else:
        adjust_sPos = gene_ePos + 1 - end
        adjust_ePos = gene_ePos + 1 - start

    fo.write('\t'.join(map(str, [gene_chrom, source, adjust_feature, adjust_sPos, adjust_ePos, '.', gene_strand, frame, description])) + '\n')
fo.close()