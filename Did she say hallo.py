def validate_hello(greetings):
    data = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]

    return any(i in greetings.lower() for i in data)
