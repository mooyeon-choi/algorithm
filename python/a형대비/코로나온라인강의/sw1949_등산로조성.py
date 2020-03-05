def back(x, y, now, use, cnt):
    global answer
    for i in range(4):
        if 0 <= x + dirs[i][0] < N and 0 <= y + dirs[i][1] < N:
            if not visit[x + dirs[i][0]][y + dirs[i][1]]:
                visit[x + dirs[i][0]][y + dirs[i][1]] = 1
                if board[x + dirs[i][0]][y + dirs[i][1]] < now:
                    back(x + dirs[i][0], y + dirs[i][1], board[x + dirs[i][0]][y + dirs[i][1]], use, cnt + 1)
                elif board[x + dirs[i][0]][y + dirs[i][1]] < now + use:
                    back(x + dirs[i][0], y + dirs[i][1], now - 1, 0, cnt + 1)
                visit[x + dirs[i][0]][y + dirs[i][1]] = 0
    if cnt > answer:
        answer = cnt


dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for tc in range(1, int(input()) + 1):
    answer = 1
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxnum = 0
    for b in board:
        if max(b) > maxnum:
            maxnum = max(b)
    for i in range(N):
        for j in range(N):
            if board[i][j] == maxnum:
                visit = [[0]*N for _ in range(N)]
                visit[i][j] = 1
                back(i, j, maxnum, K, 1)
    print(f'#{tc} {answer}')