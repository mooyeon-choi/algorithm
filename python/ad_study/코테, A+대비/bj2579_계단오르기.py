N = int(input())
board = [int(input()) for _ in range(N)]
memo = [[0, 0]] * N
for i in range(N):
    if not i:
        memo[i] = [board[i], board[i]]
    elif i == 1:
        memo[i] = [board[i], memo[0][0] + board[i]]
    else:
        memo[i] = [board[i] + max(memo[i-2]), board[i] + memo[i-1][0]]
print(max(memo[N-1]))