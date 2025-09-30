geneID=$1
seqID=$2
feature=mrna

exonerate --model est2genome --target ../01.gene_lift/gene/${geneID}.gene.fa --query ../source/${feature}/${seqID}.${feature}.fa  --showtargetgff true --showalignment false --bestn 1 > gff2/${seqID}.${feature}.gff2
python pipe/exonerate_parser.py ${seqID} ${feature}