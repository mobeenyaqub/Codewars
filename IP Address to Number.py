def ip_to_num(ip):
    ipp = []
    for i in ip.split('.'):
        ans = ''
        num = int(i)
        while num > 0:
            ans += str(num % 2)
            num //= 2

        if len(ans) < 8:
            ans += '0' * (8 - len(ans))
        ipp.append(ans[::-1])
    ipp = ''.join(ipp)
    return int(ipp, 2)


def num_to_ip(num):
    ans = ''
    ipp = []
    while num > 0:
        ans += str(num % 2)
        num //= 2
        if len(ans) == 8:
            ipp.append(int(ans[::-1], 2))
            ans = ''

    if len(ans) < 8 and len(ans) != 0:
        ans += '0' * (8 - len(ans))
        ipp.append(int(ans[::-1], 2))

    while len(ipp) < 4:
        ipp.append('0')

    return '.'.join(map(str, ipp[::-1]))
