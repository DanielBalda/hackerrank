def towerBreakers(n, m):
    towers = []
    turn = 0
    count = m-1
    for _ in range(n):
        towers.append(m)
    for index in range(len(towers)):
        if turn % 2 == 1:
            while count > 0:
                if m % count == 0:
                    towers[index] -= count
                    break
                count -= 1
        else:
            print(turn)
        turn += 1
    print(towers[1])


towerBreakers(2, 6)
