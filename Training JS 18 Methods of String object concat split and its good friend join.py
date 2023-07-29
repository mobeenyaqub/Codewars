def split_and_merge(string_, separator):
    return ' '.join([separator.join(i) for i in string_.split()])
    