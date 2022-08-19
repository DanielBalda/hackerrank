def lonelyinteger(a):
    for element in a:
        if a.count(element) == 1:
            return element


if __name__ == '__main__':
    lonelyinteger([1, 2, 3, 4, 3, 2, 1])