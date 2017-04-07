import sys
def split_file(filename):
    filecount=0
    N=int(input())
    with open(filename) as f:
        text=f.readlines()
    if len(text) % N != 0:
        raise Exception("Undividable by N=%d" % N)
    else:
        splitline = len(text) / N
    for  i in range(len(text)):
        if(i%splitline==0):
            filecount+=1
            writefilename='splitfile%d.txt'%filecount
            if(filecount>1):
                wf.close()
            wf=open(writefilename,'w')
        wf.write(text[i])
if __name__ == '__main__':
    try:
        split_file(sys.argv[1])
    except Exception as err:
        print("Error:",err)
