import collections as col

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
W, H = map(int, input().split())
board = [list(input()) for _ in range(H)]


def find_start():
    for i in range(H):
        for j in range(W):
            if board[i][j] == 'C':
                return (i, j)


def BFS(x, y):
    que = col.deque()
    for k in range(4):
        que.append((x, y, k, 0))
    while que:
        i, j, k, cnt = que.popleft()
        board[i][j] = '*'
        if 0 <= i + dirs[k][0] < H and 0 <= j + dirs[k][1] < W:
            if board[i + dirs[k][0]][j + dirs[k][1]] == 'C':
                return cnt
            elif board[i + dirs[k][0]][j + dirs[k][1]] == '.':
                for l in range(4):
                    if 0 <= i + dirs[k][0] + dirs[l][0] < H and 0 <= j + dirs[k][1] + dirs[l][1] < W:
                        if board[i + dirs[k][0] + dirs[l][0]][j + dirs[k][1] + dirs[l][1]] != '*':
                            if l != k:
                                if board[i + dirs[k][0] + dirs[l][0]][j + dirs[k][1] + dirs[l][1]] == 'C':
                                    return cnt + 1
                                que.append((i + dirs[k][0], j + dirs[k][1], l, cnt + 1))

                            else:
                                if board[i + dirs[k][0] + dirs[l][0]][j + dirs[k][1] + dirs[l][1]] == 'C':
                                    return cnt
                                que.append((i + dirs[k][0], j + dirs[k][1], l, cnt))


si, sj = find_start()
print(BFS(si, sj))
