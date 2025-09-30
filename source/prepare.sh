python pipe/gene2mrna.py

python pipe/extract_gene.py

gffread gene.gff3 \
  -g ref.fa \
  -w mrna.fa \
  -x cds.fa \
  -y protein.fa

python pipe/split.py mrna

python pipe/split.py cds
