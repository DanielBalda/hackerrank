def caesarCipher(s, k):
    abc = []
    s = list(s)
    for index in range(26):
        abc.append(chr(index+97))
    for index, letter in enumerate(s):
        if letter.lower() in abc:
            if letter.isupper():
                s[index] = (abc[(abc.index(s[index].lower()) +
                            k) % len(abc)]).upper()
            else:
                s[index] = abc[(abc.index(s[index]) +
                                k) % len(abc)]
    print(''.join(s))


if __name__ == '__main__':
    n = 11
    s = "middle-Outz"
    k = 2
    caesarCipher(s, k)
