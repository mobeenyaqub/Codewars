def to_csv_text(array):
    return '\n'.join([','.join(list(map(str, i))) for i in array])
