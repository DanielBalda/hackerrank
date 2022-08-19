def miniMaxSum(arr):
    result = 0
    for element in arr:
        result += element
    print(str(result - max(arr)) + ' ' + str(result - min(arr)))


if __name__ == '__main__':
    miniMaxSum([1, 3, 5, 7, 9])
