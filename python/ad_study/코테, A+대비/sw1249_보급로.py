def find(i, j):
    que = [(i, j)]
    while que:
        x, y = que.pop(0)
        if x + y == 2*N - 2:
            return memo[x][y]
        for k in range(4):
            if 0 <= x + dirs[k][0] < N and 0 <= y + dirs[k][1] < N:
                if memo[x][y] + board[x + dirs[k][0]][y + dirs[k][1]] < memo[x + dirs[k][0]][y + dirs[k][1]]:
                    memo[x + dirs[k][0]][y + dirs[k][1]] = memo[x][y] + board[x + dirs[k][0]][y + dirs[k][1]]
                    que.append((x + dirs[k][0], y + dirs[k][1]))


dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    memo = [[0xffffff] * N for _ in range(N)]
    memo[0][0] = 0
    print('#{} {}'.format(tc, find(0, 0)))