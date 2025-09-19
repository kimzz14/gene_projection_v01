class FastaHandler:
    def __init__(self, fastaName):
        self.fastaName = fastaName
        
        self.rcNucl_DICT = {}
        self.rcNucl_DICT['A'] = 'T'
        self.rcNucl_DICT['T'] = 'A'
        self.rcNucl_DICT['G'] = 'C'
        self.rcNucl_DICT['C'] = 'G'
        self.rcNucl_DICT['N'] = 'N'

        self.ref_DICT = {}
        self.seqName_LIST = []

        self.open_fasta(self.fastaName)

     
    def open_fasta(self, fastaFile):
        fi = open(fastaFile)

        for line in fi:
            if line.startswith('>') == True:
                seqName = line.rstrip('\n')[1:]
                self.seqName_LIST += [seqName]
                self.ref_DICT[seqName] = []
            else:
                sequence = line.rstrip('\n')
                self.ref_DICT[seqName] += [sequence]
        fi.close()

        for seqName in self.seqName_LIST:
            self.ref_DICT[seqName] = ''.join(self.ref_DICT[seqName])


    def reverse_complementary(self,sequence):
        result = []
        for nucl in sequence[::-1]:
            result += [self.rcNucl_DICT[nucl]]
        return ''.join(result) 

    def get_seq(self, seqName, strand, sPos, ePos):
        sequence = self.ref_DICT[seqName][sPos - 1:ePos]

        if strand == '+':
            pass
        elif strand == '-':
            sequence = self.reverse_complementary(sequence)
        else:
            return None
            
        return sequence        

target = 'Keumkang_v1.0.0'

ref = FastaHandler(f'../db/{target}/ref.fa')
fi = open('gene.list')

legend_LIST = fi.readline().rstrip('\n').split('\t')

geneN = 0
for line in fi:
    data_LIST = line.rstrip('\n').split('\t')
    fields = {key:value for key, value in zip(legend_LIST, data_LIST)}

    geneID = fields['geneID']
    chrom = fields['chrom']
    strand = fields['strand']
    sPos = int(fields['sbjct_sPos'])
    ePos = int(fields['sbjct_ePos'])
    fo = open(f'gene/{geneID}.gene.fa', 'w')
    fo.write(f'>{geneID}:{chrom}:{strand}:{sPos}:{ePos}\n')
    fo.write(ref.get_seq(chrom, strand, sPos, ePos) + '\n')
    fo.close()
    geneN += 1

print(geneN)