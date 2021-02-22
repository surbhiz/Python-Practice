def calculateMinimumHP(self, dungeon):
    rLen = len(dungeon)
    if rLen == 0:
        return 0
    cLen = len(dungeon[0])
    dungeon[rLen-1][cLen-1] = min(dungeon[rLen-1][cLen-1], 0)
    for r in reversed(range(rLen)):
        for c in reversed(range(cLen)):
            if r < rLen-1 or c < cLen-1:
                if c == cLen-1 and r < rLen-1:
                    dungeon[r][c] = min(0, dungeon[r][c] + dungeon[r+1][c])
                    print(dungeon[r][c])
                elif c < cLen-1 and r == rLen-1:
                    dungeon[r][c] = min(0, dungeon[r][c] + dungeon[r][c+1])
                    print(dungeon[r][c])
                else:
                    dungeon[r][c] = min(
                        0, dungeon[r][c] + max(dungeon[r][c+1], dungeon[r+1][c]))
                    print(dungeon[r][c])
    return print(abs(dungeon[0][0]) + 1)


a = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
calculateMinimumHP([], a)
