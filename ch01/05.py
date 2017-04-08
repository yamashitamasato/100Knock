def ngram(text,n,mode):
    result=[]
    if(mode=='char'):
        words=text.split(' ')
        for i in range(len(words)-n+1):
            wordlist=[]
            for j in range(0,n):
                wordlist.append(words[i+j])
            result.append(wordlist[0:n])

    elif(mode=='word'):
        word=text.replace(" ","")
        if(len(word)>n):
            for i in range(len(word)-n+1):
                result.append(word[i:i+n])
    return result
if __name__ == '__main__':
    print(ngram('I am an NLPer',2,'char'))
    print(ngram('I am an NLPer',2,'word'))
