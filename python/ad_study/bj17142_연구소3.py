import collections as col

def BFS(i, j):
    que = col.deque()
    que.append((i, j))
    virus[i][j] = 0
    count = 1
    while que:
        for _ in range(len(que)):
            u, v = que.popleft()
            for n in range(4):
                if 0 <= u + dirs[n][0] < N and 0 <= v + dirs[n][1] < N:
                    if virus[u + dirs[n][0]][v + dirs[n][1]] == -1:
                        if board[u + dirs[n][0]][v + dirs[n][1]] == 0:
                            virus[u + dirs[n][0]][v + dirs[n][1]] = count
                            que.append((u + dirs[n][0], v + dirs[n][1]))
                        elif board[u + dirs[n][0]][v + dirs[n][1]] == 2:
                            virus[u + dirs[n][0]][v + dirs[n][1]] = 0
                            que.append((u + dirs[n][0], v + dirs[n][1]))
        count += 1
    for i in range(N):
        for j in range(N):
            if not board[i][j] and virus[i][j] == -1:
                virus[i][j] = 999


def DFS(idxs):
    global answer
    if len(idxs) >= M:
        maxnum = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] != 1:
                    num = 999
                    for k in range(M):
                        if num > sprays[idxs[k]][i][j]:
                            num = sprays[idxs[k]][i][j]
                    if maxnum < num:
                        maxnum = num
                if maxnum >= answer:
                    return
        if answer > maxnum:
            answer = maxnum
        return

    for i in range(len(sprays)):
        if not used[i]:
            used[i] = 1
            DFS(idxs + [i])
            used[i] = 0

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sprays = []
answer = 999
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus = [[-1]*N for _ in range(N)]
            BFS(i, j)
            sprays.append(virus)

used = [0]*len(sprays)
DFS([])

if answer == 999:
    answer = -1

print(answer)