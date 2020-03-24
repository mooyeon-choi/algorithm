from collections import deque

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def BFS():
    count = 0
    que = deque([(0, 0)])
    while que:
        i, j = que.popleft()
        for d in range(4):
            if 0 <= i + dirs[d][0] < N and 0 <= j + dirs[d][1] < M:
                if not visit[i + dirs[d][0]][j + dirs[d][1]]:
                    if board[i + dirs[d][0]][j + dirs[d][1]]:
                        board[i + dirs[d][0]][j + dirs[d][1]] = 0
                        visit[i + dirs[d][0]][j + dirs[d][1]] = 1
                        count += 1
                    else:
                        visit[i + dirs[d][0]][j + dirs[d][1]] = 1
                        que.append((i + dirs[d][0], j + dirs[d][1]))
    return count

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

while sum(map(lambda b: sum(b), board)):
    visit = [[0] * M for _ in range(N)]
    nums = BFS()
    answer += 1

print(answer)
print(nums)