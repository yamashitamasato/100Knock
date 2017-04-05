def textmake(x,y,z):
    if(type(x)!=str):
        x=str(x)
    if(type(y)!=str):
        y=str(y)
    if(type(z)!=str):
        z=str(z)
    return(x+"時の"+y+"は"+z)
if __name__ == '__main__':
    print(textmake(12,"気温",22.4))
