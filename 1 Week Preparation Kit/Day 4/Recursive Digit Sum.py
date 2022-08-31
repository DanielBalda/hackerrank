# n = string con numeros Ej. "123"
# k = multiplicador del string Ej. si k= 3 ---> n = "123"*3 ---> 6*3 ----> 18
def superDigit(n, k):
    if len(n) == 1:
        return n
    return superDigit(str(sum(map(int, (n*k)))), 1)


print(superDigit('148', 3))
