def flippingBits(n):
    binario = list('{:032b}'.format(n))
    for index in range(len(binario)):
        if binario[index] == '1':
            binario[index] = '0'
        else:
            binario[index] = '1'
    return int(''.join(binario), 2)


#print(flippingBits(0))


def pangrama(s):
    return "pangram" if len(set(s.lower())) == 26 else "not pangram"
    # abc = [chr(index) for index in range(97, 123)]
    # for element in s.replace(" ", "").lower():
    #     abc.remove(element) if element in abc else None
    # return "pangram" if len(abc) == 0 else "not pangram"


#print(
#        pangrama("abcdefghijk  lmnopqrstuvwxyz"),
#        pangrama("abcdefghijklmn  opqrstuvwxya")
#    )


def birthday(s, d, m):
    longitud = len(s)
    if longitud > 1:
        for pos in range(0, len(s), m):
            print(pos)
    else:
        if longitud == m and s[0] == d:
            return 1
        else:
            return 0


birthday([1, 1, 1, 1, 1, 1], 3, 2)


class calculadora():
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def suma(self, num1, num2):
        return num1+num2


calcu = calculadora()
print(calcu.suma(1, 2))