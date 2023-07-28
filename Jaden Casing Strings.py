def to_jaden_case(string):
    return ' '.join(i[0].upper() + i[1:].lower() for i in string.split())