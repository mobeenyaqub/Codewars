def to_twos_complement(binary, bits):
    binary = list(map(int, ''.join(binary.split())))[::-1]

    ans = 0
    for i in range(len(binary) - 1):
        ans += binary[i] * 2 ** i

    return ans - binary[-1] * 2 ** (bits - 1)


def from_twos_complement(n, bits):
    positive = True if n >= 0 else False
    ans = ''
    if n >= 0:
        while n > 0:
            ans += str(n % 2)
            n //= 2
    else:
        ans += '1'
        check = (2 ** (bits - 1)) * -1
        power = bits - 2
        while check != n:
            c = 2 ** power
            if check + c <= n:
                check += c
                ans += '1'
            else:
                ans += '0'
            power -= 1

    if len(ans) != bits:
        ans += '0' * (bits - len(ans))

    return ans if not positive else ans[::-1]
