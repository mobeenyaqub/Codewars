def html_special_chars(data):
    ans = ""
    for i in data:
        if i == "<":
            ans += "&lt;"
        elif i == ">":
            ans += "&gt;"
        elif i == '"':
            ans += "&quot;"
        elif i == "&":
            ans += "&amp;"
        else:
            ans += i

    return ans
