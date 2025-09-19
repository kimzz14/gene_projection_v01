fi = open('cds.fa')
fo_list = open('cds.list', 'w')
fo = None
for line in fi:
    if line.startswith('>'):
        cdsID = line.rstrip('\n').split('\t')[0][1:]

        if fo != None: fo.close()

        fo_list.write(cdsID + '\n')

        fo = open(f'cds/{cdsID}.cds.fa', 'w')
        fo.write(f'>{cdsID}\n')
    else:
        fo.write(line)    
fi.close()
fo.close()
fo_list.close()