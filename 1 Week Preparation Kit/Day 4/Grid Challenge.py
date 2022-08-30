def gridChallenge(grid):
    count = 0
    for index in range(len(grid[0])):
        compare = 0
        for row in grid:
            row = sorted(row)
            if compare <= ord(row[index]):
                compare = ord(row[index])
                count += 1
    return "YES" if count == len(grid[0])*len(grid) else "NO"


gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
gridChallenge(['ebacf', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
gridChallenge(['mpxz', 'abcd', 'wlmf'])
gridChallenge(['vpvv', 'pvvv', 'vzzp', 'zzyy'])
