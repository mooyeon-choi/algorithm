def water():
    que = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == '*':
                board[i][j] = 0
                for k in range(4):
                    if 0 <= i + dirs[k][0] < R and 0 <= j + dirs[k][1] < C:
                        if board[i + dirs[k][0]][j + dirs[k][1]] == '.':
                            que.append((i, j))
                            break
    cnt = 1
    while que:
        for _ in range(len(que)):
            u, v = que.pop(0)
            for k in range(4):
                if 0 <= u + dirs[k][0] < R and 0 <= v + dirs[k][1] < C:
                    if board[u + dirs[k][0]][v + dirs[k][1]] == '.':
                        board[u + dirs[k][0]][v + dirs[k][1]] = cnt
                        que.append((u + dirs[k][0], v + dirs[k][1]))
        cnt += 1


def BFS(i, j):
    global answer
    que = []
    que.append((i, j))
    cnt = 1
    while que:
        if cnt > max_num:
            return
        for _ in range(len(que)):
            u, v = que.pop(0)
            for k in range(4):
                if 0 <= u + dirs[k][0] < R and 0 <= v + dirs[k][1] < C:
                    if board[u + dirs[k][0]][v + dirs[k][1]] == 'D':
                        answer = cnt
                        return
                    elif board[u + dirs[k][0]][v + dirs[k][1]] > cnt:
                        que.append((u + dirs[k][0], v + dirs[k][1]))
        cnt += 1


answer = 'KAKTUS'
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
water()
max_num = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == 'X':
            board[i][j] = 0
        elif board[i][j] == '.':
            board[i][j] = 9999

for i in range(R):
    for j in range(C):
        if board[i][j] == 'D':
            for k in range(4):
                if 0 <= i + dirs[k][0] < R and 0 <= j + dirs[k][1] < C:
                    if board[i + dirs[k][0]][j + dirs[k][1]] > max_num:
                        max_num = board[i + dirs[k][0]][j + dirs[k][1]]

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            board[i][j] = 0
            BFS(i, j)

print(answer)
