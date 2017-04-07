import sys
N=int(input())
with open(sys.argv[1]) as f:
    text=f.readlines()
    for i in range(N):
        print(text[i],end="")
