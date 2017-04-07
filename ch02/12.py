import sys
with open(sys.argv[1]) as f:
    with open('col1.txt', 'w') as fw1:
        with open('col2.txt', 'w') as fw2:
            for line in f:
                word=line.split('\t')
                fw1.write(word[0]+'\n')
                fw2.write(word[1]+'\n')
