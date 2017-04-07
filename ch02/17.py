import sys
onelinelist=set()
with open(sys.argv[1]) as f:
    for text in f:
        word=text.split('\t')
        onelinelist.add(word[0])
for word in onelinelist:
    print(word)
