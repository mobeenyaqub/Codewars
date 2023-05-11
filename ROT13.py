import string


def rot13(message):
    new_message = ""
    for character in message:
        key = character
        if character.isalpha():
            try:
                key = string.ascii_lowercase[(
                    string.ascii_lowercase.index(character) + 13) % 26]
            except:
                key = string.ascii_uppercase[(
                    string.ascii_uppercase.index(character) + 13) % 26]
        new_message += key

    return new_message
