
def removeUselessCharacters(itemsList):
    items = []
    itemsList = itemsList.split(' ')
    print(itemsList, 'items!!!!')

    for item in itemsList:
        item = item.replace(')', ' ')
        item = item.replace('(', ' ') 
        item = item.replace('/', ' ') 
        item = item.replace('|', ' ') 
        items.append(item)
    if len(items) == 3:
        return items
    return False