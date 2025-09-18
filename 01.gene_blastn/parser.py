def read_blastn(geneID):
    fi = open(f'result2/{geneID}.blastn')
    for line in fi:
        query, sbjct, identity, alignment_length, mismatches, gap_openings, query_sPos, query_ePos, sbjct_sPos, sbjct_ePos, e_value, bit_score = line.rstrip('\n').split('\t')
        identity = float(identity)/100
        alignment_length = int(alignment_length)
        mismatches = int(mismatches)
        gap_openings = int(gap_openings)
        query_sPos = int(query_sPos)
        query_ePos = int(query_ePos)
        sbjct_sPos = int(sbjct_sPos)
        sbjct_ePos = int(sbjct_ePos)

        #print(query, sbjct, identity, alignment_length, mismatches, gap_openings, query_sPos, query_ePos, sbjct_sPos, sbjct_ePos, e_value, bit_score)
        _geneID, chrom, strand, gene_sPos, gene_ePos = query.split(':')
        gene_sPos = int(gene_sPos)
        gene_ePos = int(gene_ePos)

        gene_length = gene_ePos - gene_sPos + 1


        coverage = alignment_length / gene_length

        if sbjct_sPos < sbjct_ePos:
            if strand == '+':
                print(f'{_geneID}\t{sbjct}\t{'+'}\t{sbjct_sPos}\t{sbjct_ePos}\t{coverage}\t{identity}')
            else:
                print(f'{_geneID}\t{sbjct}\t{'-'}\t{sbjct_sPos}\t{sbjct_ePos}\t{coverage}\t{identity}')
        else:
            if strand == '+':
                print(f'{_geneID}\t{sbjct}\t{'-'}\t{sbjct_ePos}\t{sbjct_sPos}\t{coverage}\t{identity}')
            else:
                print(f'{_geneID}\t{sbjct}\t{'+'}\t{sbjct_ePos}\t{sbjct_sPos}\t{coverage}\t{identity}')

        break
    fi.close()

fi = open('gene.list')

for line in fi:
    geneID = line.rstrip('\n')
    read_blastn(geneID)
