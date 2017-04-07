with open('col1.txt','r') as fr1, open('col2.txt','r') as fr2:
    line1,line2=fr1.readlines(),fr2.readlines()
with open('result.txt','w') as fw:
    for text1,text2 in zip(line1,line2):
        fw.write(text1.replace('\n', '\t')+text2)
