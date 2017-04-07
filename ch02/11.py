import sys
with open(sys.argv[1]) as f:
    str=f.read()
print(str.replace('\t', ' '),end="")
