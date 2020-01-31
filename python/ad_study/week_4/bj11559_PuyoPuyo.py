def BFS(i, j, alpa):
    que = []
    que.append((i, j))
    idx = 0
    while idx < len(que):
        u, v = que[idx]
        visit[u][v] = 1
        for k in range(4):
            if 0 <= u + dirs[k][0] < 12 and 0 <= v + dirs[k][1] < 6:
                if board[u + dirs[k][0]][v + dirs[k][1]] == alpa:
                    if (u + dirs[k][0], v + dirs[k][1]) not in que:
                        que.append((u + dirs[k][0], v + dirs[k][1]))
        idx += 1
    if len(que) >= 4:
        for k in range(len(que)):
            board[que[k][0]][que[k][1]] = '.'
            cnt[que[k][1]] += 1
        return True
    else:
        return False


def block_down():
    for i in range(6):
        if height[i] < 12:
            first, second = 11, 11
            while True:
                if first < 0:
                    break
                if board[first][i] != '.':
                    first -= 1
                else:
                    if second < height[i]:
                        break
                    elif second >= first or board[second][i] == '.':
                        second -= 1
                    else:
                        board[first][i], board[second][i] = board[second][i], board[first][i]


answer = -1
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
board = [list(input()) for _ in range(12)]
height = [12]*6
for i in range(12):
    for j in range(6):
        if height[j] == 12 and board[i][j] != '.':
            height[j] = i
bomb = 1
while bomb:
    visit = [[0]*6 for _ in range(12)]
    cnt = [0]*6
    bomb = 0
    for i in range(min(height), 12):
        for j in range(6):
            if board[i][j] != '.' and not visit[i][j]:
                if BFS(i, j, board[i][j]):
                    bomb = 1
    block_down()
    for i in range(6):
        height[i] += cnt[i]
    answer += 1

print(answer)