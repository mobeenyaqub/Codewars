def find_missing_letter(chars):
    for i in range(len(chars)):
        if ord(chars[i]) + 1 != ord(chars[i+1]):
            return chr(ord(chars[i]) + 1)
