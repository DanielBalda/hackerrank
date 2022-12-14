def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


test_cases = int(1)
for cs in range(test_cases):
    n = int(9)
    a = list(map(int, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    findZigZagSequence(a, n)
