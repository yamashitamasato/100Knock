import sys
onelinedict={}
with open(sys.argv[1]) as f:
    text=f.readlines()
    for word in text:
        word=word.split('\t')[0]
        if(word not in onelinedict):
            onelinedict.update({word:1})
        else:
            onelinedict[word]=onelinedict[word]+1

for key in sorted(onelinedict.items(), key=lambda x: x[1], reverse=True):
    print(key[0])
