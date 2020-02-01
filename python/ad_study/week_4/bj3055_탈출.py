import collections as col

def BFS():
    global answer
    que = col.deque()
    for i in range(R):
        for j in range(C):
            if board[i][j] == '*':
               que.append((i, j, board[i][j]))
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'S':
               que.append((i, j, board[i][j]))
    cnt = 1
    while que:
        for _ in range(len(que)):
            u, v, alpha = que.popleft()
            for k in range(4):
                if 0 <= u + dirs[k][0] < R and 0 <= v + dirs[k][1] < C:
                    if alpha == 'S' and board[u + dirs[k][0]][v + dirs[k][1]] == 'D':
                        answer = cnt
                        return
                    elif not visit[u + dirs[k][0]][v + dirs[k][1]] and board[u + dirs[k][0]][v + dirs[k][1]] == '.':
                        visit[u + dirs[k][0]][v + dirs[k][1]] = 1
                        que.append((u + dirs[k][0], v + dirs[k][1], alpha))
        cnt += 1


answer = 'KAKTUS'
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visit = [[0]*C for _ in range(R)]
BFS()
print(answer)
