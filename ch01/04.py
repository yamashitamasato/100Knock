text="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words=text.split(" ")
i=1
dict={}
one_wordlist=[1,5,6,7,8,9,15,16,19]
for word in words:
    if(i in one_wordlist):
        dict.update({i:word[0]})
    else:
        dict.update({i:word[0:2]})
    i+=1
print(dict)
