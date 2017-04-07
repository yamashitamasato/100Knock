import sys
with open(sys.argv[1]) as f:
    text=f.readlines()
for word in sorted(text, key=lambda x: x.split()[2], reverse=True):
    print(word,end="")
