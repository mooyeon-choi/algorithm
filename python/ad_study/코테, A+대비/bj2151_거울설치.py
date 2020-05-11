import collections as col

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())
board = [list(input()) for _ in range(N)]
answer = 2500
visit = set()

for i in range(N):
    for j in range(N):
        if board[i][j] == '#' and answer == 2500:
            que = col.deque()
            for k in range(4):
                que.append((i, j, k, 0))
            while que:
                x, y, d, cnt = que.popleft()
                while 0 <= x < N and 0 <= y < N and board[x][y] != '*' and cnt < answer:
                    x += dirs[d][0]
                    y += dirs[d][1]
                    if not (0 <= x < N and 0 <= y < N):
                        break
                    if (x != i or y != j) and board[x][y] == '#':
                        answer = cnt
                        break
                    if board[x][y] == '!':
                        visit.add((x, y, d))
                        for u in range(4):
                            if (x, y, u) not in visit:
                                if d // 2:
                                    if not u // 2:
                                        visit.add((x, y, u))
                                        que.append((x, y, u, cnt + 1))
                                else:
                                    if u // 2:
                                        visit.add((x, y, u))
                                        que.append((x, y, u, cnt + 1))

print(answer)