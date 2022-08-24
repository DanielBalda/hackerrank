def towerBreakers(n, m):
    towers = []
    turn = 0
    for _ in range(n):
        towers.append(m)
    for index in range(len(towers)):
        if turn % 2 == 1:
            print(turn)
        else:
            print(turn)
        turn += 1


towerBreakers(2, 2)
