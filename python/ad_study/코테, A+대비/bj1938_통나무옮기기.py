dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())
answer = 0
board = [list(input()) for _ in range(N)]
visit = [[0xfffffff]*N for _ in range(N)]
status = 0
first = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            if first:
                if not status:
                    if first[0] < i:
                        status = (i, j, False)
                    else:
                        status = (i, j, True)
            first = (i, j)

def DFS(x, y, z, c):
    global answer
    if answer and c > answer:
        return
    if z:
        if board[x][y - 1] == 'E':
            if board[x][y] == 'E':
                if board[x][y + 1] == 'E':
                    if not answer or answer > c:
                        answer = c
    else:
        if board[x - 1][y] == 'E':
            if board[x][y] == 'E':
                if board[x + 1][y] == 'E':
                    if not answer or answer > c:
                        answer = c
    for i in range(4):
        if z:
            if 0 <= x + dirs[i][0] < N and 0 <= y + dirs[i][1]*2 < N:
                if board[x + dirs[i][0]][y + dirs[i][1]] != '1':
                    if board[x + dirs[i][0]][y - 1 + dirs[i][1]] != '1':
                        if board[x + dirs[i][0]][y + 1 + dirs[i][1]] != '1':
                            if c < visit[x + dirs[i][0]][y + dirs[i][1]]:
                                visit[x + dirs[i][0]][y + dirs[i][1]] = c
                                DFS(x + dirs[i][0], y + dirs[i][1], z, c + 1)
        else:
            if 0 <= x + dirs[i][0]*2 < N and 0 <= y + dirs[i][1] < N:
                if board[x + dirs[i][0]][y + dirs[i][1]] != '1':
                    if board[x - 1 + dirs[i][0]][y + dirs[i][1]] != '1':
                        if board[x + 1 + dirs[i][0]][y + dirs[i][1]] != '1':
                            if c < visit[x + dirs[i][0]][y + dirs[i][1]]:
                                visit[x + dirs[i][0]][y + dirs[i][1]] = c
                                DFS(x + dirs[i][0], y + dirs[i][1], z, c + 1)
    cnt = 0
    for i in range(3):
        for j in range(3):
            if 0 <= x + i - 1 < N and 0 <= y + j - 1 < N:
                if board[x + i - 1][y + j - 1] != '1':
                    cnt += 1
    if c <= visit[x][y] + 1 and cnt == 9:
        visit[x][y] = c
        DFS(x, y, not z, c + 1)

DFS(status[0], status[1], status[2], 0)
print(answer)