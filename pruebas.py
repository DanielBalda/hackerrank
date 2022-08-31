def flippingBits(n):
    binario = list('{:032b}'.format(n))
    for index in range(len(binario)):
        if binario[index] == '1':
            binario[index] = '0'
        else:
            binario[index] = '1'
    return int(''.join(binario), 2)


print(flippingBits(0))


def pangrama(s):
    abc = [chr(index) for index in range(97, 123)]
    for element in s.replace(" ", "").lower():
        abc.remove(element) if element in abc else None
    return "pangram" if len(abc) == 0 else "not pangram"
