def ngram(text,n,mode):
    result=[]
    if(mode=='char'):
        words=text.split(' ')
        for i in range(len(words)-n+1):
            result.append([words[i],words[i+1]])
    elif(mode=='word'):
        word=text.replace(" ","")
        if(len(word)>n):
            for i in range(len(word)-n+1):
                result.append(word[i:i+n])
    return result
if __name__ == '__main__':
    print(ngram('I am an NLPer',2,'char'))
    print(ngram('I am an NLPer',2,'word'))
