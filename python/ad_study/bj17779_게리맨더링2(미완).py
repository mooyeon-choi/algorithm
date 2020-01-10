def DFS(x, y, height, width):
    for i in range(x):
        region[1] += sum(board[i][:y+1])
        region[2] += sum(board[i][y+1:])
    if width < max_len:

    else:
        if height < max_len // 1 + 1 + (total_len - max_len):
            if y - 1 > 0:




N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0xffffff
region = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for max_len in range(1, N + 1, 2):
    for total_len in range(max_len, N + 1):
        for i in range(N):
            for j in range(max_len - 1, N - max_len + 1):
                for 

print()