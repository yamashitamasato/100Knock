import sys
N=int(input())
with open(sys.argv[1]) as f:
    text=f.readlines()
    for i in range(N,0,-1):
        print(text[len(text)-i],end="")
