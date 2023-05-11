def make_readable(seconds):
    h = m = s = "00"

    if seconds >= 3600:
        if seconds // 3600 >= 10:
            h = str(seconds // 3600)
        else:
            h = "0" + str(seconds // 3600)
        seconds = seconds % 3600

    if seconds >= 60:
        if seconds // 60 >= 10:
            m = str(seconds // 60)
        else:
            m = "0" + str(seconds // 60)
        seconds = seconds % 60

    if len(str(seconds)) < 2:
        s = "0" + str(seconds)
    else:
        s = str(seconds)

    return h + ":" + m + ":" + s
