
def removeUselessCharacters(itemsList):
    items = []
    for item in itemsList:

        item = item.replace(')', ' ')
        item = item.replace('(', ' ') 
        item = item.replace('/', ' ') 
        item = item.replace('|', ' ') 
        items.append(item)
    return items