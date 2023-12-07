def oxford_comma(items):
    if len(items) >= 3:
        items[-1] = "and " + items[-1]
        listed_items = ', '.join(items)
        pass
    elif len(items) == 2:
        listed_items = ' and '.join(items)
    else:
        listed_items = ', '.join(items)
    return listed_items
    
