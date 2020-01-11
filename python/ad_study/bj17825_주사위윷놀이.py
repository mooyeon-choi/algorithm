def DFS(count, point):
    global answer
    if answer < point:
        print(pieces)
        answer = point
        print(answer)
    if count == 10:
        return
    for i in range(4):
        resist = pieces[i]
        cnt = 0
        if pieces[i] != 40:
            if not lines[i]:
                while cnt < orders[count]:
                    pieces[i] = outside[pieces[i]]
                    cnt += 1
                if pieces[i] != 40:
                    for j in range(4):
                        if j != i and pieces[i] == pieces[j] and (not pieces[i] % 10 or lines[i] == lines[j]):
                            pieces[i] = resist
                            return
                if not pieces[i] % 10:
                    lines[i] = 1
                DFS(count + 1, point + pieces[i])
                pieces[i] = resist
                lines[i] = 0
            else:
                while cnt < orders[count]:
                    pieces[i] = inside[pieces[i]]
                    cnt += 1
                if pieces[i] != 40:
                    for j in range(4):
                        if j != i and pieces[i] == pieces[j] and (not pieces[i] % 10 or lines[i] == lines[j]):
                            pieces[i] = resist
                            return
                DFS(count + 1, point + pieces[i])
                pieces[i] = resist


outside = {
    0: 2, 2: 4, 4: 6, 6: 8, 8: 10,
    10: 12, 12: 14, 14: 16, 16: 18, 18: 20,
    20: 22, 22: 24, 24: 26, 26: 28, 28: 30,
    30: 32, 32: 34, 34: 36, 36: 38, 38: 40,
    40: 40
    }
inside = {
    10: 13, 13: 16, 16: 19, 19 : 25,
    20: 22, 22: 24, 24: 25,
    30: 28, 28: 27, 27: 26, 26: 25,
    25: 30, 30: 35, 35: 40,
    40: 40
}

lines = [0, 0, 0, 0]
pieces = [0, 0, 0, 0]
answer = 0

orders = list(map(int, input().split()))
DFS(0, 0)
print(answer)
