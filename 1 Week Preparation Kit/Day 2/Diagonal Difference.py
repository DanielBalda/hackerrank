def diagonalDifference(arr):
    d = [0, 0]
    for i, r in enumerate(arr):
        d[0], d[1] = [d[0] + r[i], d[1] + r[len(arr)-1-i]]
    return abs(d[0]-d[1])


if __name__ == '__main__':
    print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
