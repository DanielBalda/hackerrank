def flippingBits(n):
    binario = list('{:032b}'.format(n))
    for index in range(len(binario)):
        if binario[index] == '1':
            binario[index] = '0'
        else:
            binario[index] = '1'
    return int(''.join(binario), 2)


print(flippingBits(0))
