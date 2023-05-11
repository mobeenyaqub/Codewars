def array(string):
    string = string.split(",")

    if len(string) <= 2:
        return None

    return ' '.join(string[1:-1])
