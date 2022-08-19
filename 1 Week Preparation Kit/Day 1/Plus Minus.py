def plusMinus(arr):
    long = len(arr)
    pos, neg, neu = 0, 0, 0
    for element in arr:
        if element == 0:
            neu += 1
        if element > 0:
            pos += 1
        if element < 0:
            neg += 1
    print("{:.6f}\n{:.6f}\n{:.6f}".format(pos/long,
                                          neg/long,
                                          neu/long))


if __name__ == '__main__':
    plusMinus([-4, 3, -9, 0, 4, 1])
