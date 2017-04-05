def cipher(word):
    charlist=list(word)
    result=""
    for char in charlist:
        if char.isalpha() & char.islower():
            result+=chr(219-ord(char))
        else:
            result+=char
    return(result)
if __name__ == '__main__':
    print(cipher("Hello World"))
