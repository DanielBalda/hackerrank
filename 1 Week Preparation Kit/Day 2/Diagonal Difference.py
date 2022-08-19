arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
count, ldiag, rdiag = 0, 0, 0
for row in arr:
    rdiag += row[count]
    ldiag += row[len(arr)-1-count]
    count += 1
    return abs(ldiag-rdiag)