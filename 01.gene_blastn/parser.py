class BLOCK:
    def __init__(self):
        self.hsp_LIST = []

        self.strand = None
        self.chrom = None

        self.query_sPos = None
        self.query_ePos = None
        self.sbjct_sPos = None
        self.sbjct_ePos = None
        self.isSet = False
    
    def set(self,gene_sPos, gene_ePos, hsp):
        self.isSet = True
        self.hsp_LIST += [hsp]

        self.strand = hsp.strand
        self.chrom = hsp.chrom

        self.query_sPos = hsp.query_sPos
        self.query_ePos = hsp.query_ePos
        
        self.sbjct_sPos = hsp.sbjct_sPos
        self.sbjct_ePos = hsp.sbjct_ePos

        self.gene_sPos = gene_sPos
        self.gene_ePos = gene_ePos

    def calc_coverage(self):
        if len(self.hsp_LIST) == 0:
            return 0.0

        return (self.query_ePos - self.query_sPos + 1) / (self.gene_ePos - self.gene_sPos + 1)

    def calc_identity(self):
        if len(self.hsp_LIST) == 0:
            return 0.0

        totalbp = 0
        matchbp = 0

        for hsp in self.hsp_LIST:
            totalbp += hsp.query_len
            matchbp += hsp.identity * hsp.query_len

        return matchbp / totalbp

    def extention(self, hsp):
        if self.hsp_LIST[0].strand != hsp.strand:
            return
        
        if self.hsp_LIST[0].chrom != hsp.chrom:
            return

        if abs(self.hsp_LIST[0].intercept - hsp.intercept) > 100:
            return
        
        self.query_sPos = min(self.query_sPos, hsp.query_sPos)
        self.query_ePos = max(self.query_ePos, hsp.query_ePos)
        if self.strand == '+':
            self.sbjct_sPos = min(self.sbjct_sPos, hsp.sbjct_sPos)
            self.sbjct_ePos = max(self.sbjct_ePos, hsp.sbjct_ePos)
        else:
            self.sbjct_sPos = max(self.sbjct_sPos, hsp.sbjct_sPos)
            self.sbjct_ePos = min(self.sbjct_ePos, hsp.sbjct_ePos)
        
        self.hsp_LIST += [hsp]
        
    def text(self):
        return f'{self.chrom}\t{self.strand}\t{self.query_sPos}\t{self.query_ePos}\t{self.sbjct_sPos}\t{self.sbjct_ePos}\t{self.calc_coverage()}\t{self.calc_identity()}\t{len(self.hsp_LIST)}'

class HSP:
    def __init__(self, chrom, identity, query_sPos, query_ePos, sbjct_sPos, sbjct_ePos):
        self.identity = identity
        self.chrom = chrom
        self.query_sPos = query_sPos
        self.query_ePos = query_ePos
        self.query_len = self.query_ePos - self.query_sPos + 1

        self.sbjct_sPos = sbjct_sPos
        self.sbjct_ePos = sbjct_ePos

        if sbjct_sPos < sbjct_ePos:
            self.strand = '+'
            self.intercept = (-self.query_sPos +self.sbjct_sPos) / 2 + (-self.query_ePos +self.sbjct_ePos) / 2
            self.sbjct_len = self.sbjct_ePos - self.sbjct_sPos + 1
        else:
            self.strand = '-'
            self.intercept = (+self.query_sPos +self.sbjct_sPos) / 2 + (+self.query_ePos +self.sbjct_ePos) / 2
            self.sbjct_len = self.sbjct_sPos - self.sbjct_ePos + 1

    def show(self):
        return f'{self.query_sPos} {self.query_ePos} {self.sbjct_sPos} {self.sbjct_ePos}'

def read_blastn(fileName):
    fi = open(fileName)
    block = BLOCK()

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

        #if identity < 0.95: continue

        _geneID, chrom, strand, gene_sPos, gene_ePos = query.split(':')
        gene_sPos = int(gene_sPos)
        gene_ePos = int(gene_ePos)

        hsp = HSP(sbjct, identity, query_sPos, query_ePos, sbjct_sPos, sbjct_ePos)
        if block.isSet == False:
            block.set(gene_sPos, gene_ePos, hsp)
        else:
            block.extention(hsp)

    fi.close()

    return block

import os
fi = open('gene.list')

for line in fi:
    geneID = line.rstrip('\n')
    fileName = f'merge/{geneID}.blastn'
    if os.path.exists(fileName):
        print(f'{geneID}\t{read_blastn(fileName).text()}')
    else:
        print(f'{geneID}')
