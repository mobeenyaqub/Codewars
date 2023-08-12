def distinct(seq):
    data = []
    
    for i in seq:
        if i not in data:
            data.append(i)
    
    return data