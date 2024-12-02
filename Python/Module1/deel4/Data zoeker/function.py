def get_value(data, separator=',', position=0):
    items = data.split(separator) 
    if position < len(items): 
        return items[position] 
    else:
        return None  
