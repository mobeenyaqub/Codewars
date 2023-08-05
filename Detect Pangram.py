from string import ascii_lowercase

def is_pangram(s):
    try:
        data = sorted(set(s.lower()))
        idx = data.index('a')
    except:
        return False
    return data[idx:] == list(ascii_lowercase)