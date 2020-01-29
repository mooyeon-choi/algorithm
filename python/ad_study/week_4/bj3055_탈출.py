import collections as col

def water(i, j):
    que = col.deque()
    que.append((i, j))
    cnt = 1
    while que:
        for _ in range(len(que)):
            u, v = que.popleft()
            for k in range(4):
                if 0 <= u + dirs[k][0] < R and 0 <= v + dirs[k][1] < C:
                    if water_count[u + dirs[k][0]][v + dirs[k][1]] > cnt and board[u + dirs[k][0]][v + dirs[k][1]] not in 'DX':
                        water_count[u + dirs[k][0]][v + dirs[k][1]] = cnt
                        que.append((u + dirs[k][0], v + dirs[k][1]))
        cnt += 1


def BFS(i, j):
    global answer
    que = col.deque()
    que.append((i, j))
    cnt = 1
    while que:
        for _ in range(len(que)):
            u, v = que.popleft()
            for k in range(4):
                if 0 <= u + dirs[k][0] < R and 0 <= v + dirs[k][1] < C:
                    if water_count[u + dirs[k][0]][v + dirs[k][1]] > cnt:
                        if board[u + dirs[k][0]][v + dirs[k][1]] == 'D':
                            answer = cnt
                            return
                        que.append((u + dirs[k][0], v + dirs[k][1]))
        cnt += 1


answer = 'KAKTUS'
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
water_count = [[99]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            water_count[i][j] = 0
            water(i, j)

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            BFS(i, j)

print(answer)

