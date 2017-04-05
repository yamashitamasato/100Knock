def ngram(text,n):
    result=[]
    word=text.replace(" ","")
    if(len(word)>n):
        for i in range(len(word)-n+1):
            result.append(word[i:i+n])
    return result
if __name__ == '__main__':
    X=set(ngram('paraparaparadise',2))
    Y=set(ngram('paragraph',2))
    print("X or Y=",X | Y)
    print("X and Y=",X & Y)
    print("X - Y=",X - Y)
    print("Y - X=",Y - X)
    if('se' in X):
        print("Find 'se' in X")
    elif('se' in Y):
        print("Find 'se' in Y")
