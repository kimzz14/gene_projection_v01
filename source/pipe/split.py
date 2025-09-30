import sys

feature = sys.argv[1]

fi = open(f'{feature}.fa')
fo_list = open(f'{feature}.list', 'w')
fo = None

countN = 0
for line in fi:
    if line.startswith('>'):
        seqName = line.rstrip('\n')[1:].split('\t')[0].split(' ')[0]
        countN += 1

        if fo != None: fo.close()

        fo_list.write(seqName + '\n')

        fo = open(f'{feature}/{seqName}.{feature}.fa', 'w')
        fo.write(f'>{seqName}\n')
    else:
        fo.write(line)    
fi.close()
fo.close()
fo_list.close()

print(countN)
