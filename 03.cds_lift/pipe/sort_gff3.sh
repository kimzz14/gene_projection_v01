prefix=$1
gffread ${prefix}.gff3 -O --sort-by ref.chrom.list -o ${prefix}.sorted.gff3
