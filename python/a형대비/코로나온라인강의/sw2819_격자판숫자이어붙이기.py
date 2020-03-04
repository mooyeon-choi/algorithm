def DFS(x, y, numbers):
    if len(numbers) >= 7:
        numset.add(numbers)
        return
    for k in range(4):
        if 0 <= x + dirs[k][0] < 4 and 0 <= y + dirs[k][1] < 4:
            DFS(x + dirs[k][0], y + dirs[k][1], numbers + board[x + dirs[k][0]][y + dirs[k][1]])


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for tc in range(1, int(input()) + 1):
    board = [input().split() for _ in range(4)]
    numset = set()
    for i in range(4):
        for j in range(4):
            DFS(i, j, board[i][j])
    print(f'#{tc} {len(numset)}')
