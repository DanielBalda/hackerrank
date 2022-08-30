def lonelyinteger(a):
    for element in a:
        return element if a.count(element) == 1 else None


if __name__ == '__main__':
    lonelyinteger([1, 2, 3, 4, 3, 2, 1])
