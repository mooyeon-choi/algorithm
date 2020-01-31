def BFS(i, j, alpa):
    nums = 1
    que = []
    que.append((i, j))
    idx = 0
    while idx < len(que):
        u, v = que[idx]
        for k in range(4):
            if 0 <= u + dirs[k][0] < 12 and 0 <= v + dirs[k][1] < 6:
                if board[u + dirs[k][0]][v + dirs[k][1]] == alpa:
                    que.append((u + dirs[k][0], v + dirs[k][1]))
                    nums += 1
    if nums >= 4:
        for k in range(len(que)):
            board[que[k][0]][que[k][1]] = '.'
        return True
    else:
        return False


def block_down():
    for i in range(6):
        first, second = 11, 11
        find = 0
        while True:
            if board[first][i] != '.':
                first -= 1
            else:
                if second >= first or board[second][i] == '.':
                    second -= 1
                elif second < height[i]:
                    break
                else:
                    board[first][i], board[second][i] = board[second][i], board[first][i]


answer = -1
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
board = [list(input()) for _ in range(12)]
height = [0]*6
for i in range(12):
    for j in range(6):
        if not height[j] and board[i][j] != '.':
            height[j] = i
bomb = 1
while bomb:
    bomb = 0
    for i in range(max(height), 12):
        for j in range(6):
            if board[i][j] != '.':
                if BFS(i, j, board[i][j]):
                    bomb = 1
    block_down()
    answer += 1

print(answer)