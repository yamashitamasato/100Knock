import random
text="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words=text.split(' ')
result=[]
for word in words:
    if(len(word)>4):
        word=list(word)
        first=word.pop(0)
        last=word.pop()
        random.shuffle(word)
        word=first+''.join(word)+last
        result.append(word)
    else:
        result.append(word)
print(' '.join(result))
