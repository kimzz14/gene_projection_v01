geneID=$1
cdsID=$2

#exonerate --model est2genome --target gene/${geneID}.gene.fa --query ../db/wheat.CS.Gapless/cds/${cdsID}.cds.fa  --showtargetgff true --showalignment false --bestn 1 > gff2/${cdsID}.gff2
python 03.exonerate_parser.py ${cdsID}