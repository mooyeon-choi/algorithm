def walls(x, y, cnt):
    global maxnum
    if cnt == 3:
        nums = BFS()
        if nums > maxnum:
            maxnum = nums
        return
    for i in range(x, N):
        if x == i:
            for j in range(y, M):
                if not board[i][j]:
                    board[i][j] = 1
                    walls(i, j, cnt + 1)
                    board[i][j] = 0
        else:
            for j in range(M):
                if not board[i][j]:
                    board[i][j] = 1
                    walls(i, j, cnt + 1)
                    board[i][j] = 0


def BFS():
    que = []
    nums = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                que.append((i, j))
                nums += 1
    cnt = 0
    while cnt < len(que):
        u, v = que[cnt]
        for k in range(4):
            if 0 <= u + dirs[k][0] < N and 0 <= v + dirs[k][1] < M:
                if not board[u + dirs[k][0]][v + dirs[k][1]]:
                    if (u + dirs[k][0], v + dirs[k][1]) not in que:
                        que.append((u + dirs[k][0], v + dirs[k][1]))
        cnt += 1
    return len(que) - nums


maxnum = 0
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = sum(list(map(lambda x: x.count(0), board)))
walls(0, 0, 0)
answer - maxnum
print(answer)

