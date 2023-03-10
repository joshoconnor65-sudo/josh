
def removeUselessCharacters(str):
    str = str.replace(')', ' ')
    str = str.replace('(', ' ') 
    str = str.replace('/', ' ') 
    str = str.replace('|', ' ') 
    return str