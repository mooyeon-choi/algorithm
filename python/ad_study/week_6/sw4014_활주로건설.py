for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    can = [1]*N*2
    for i in range(N):
        row_cnt, col_cnt = 1, 1
        row_num = board[i][0]
        col_num = board[0][i]
        for j in range(1, N):
            if board[i][j] == row_num:
                row_cnt += 1
            elif board[i][j] > row_num:
                if board[i][j] == row_num + 1:
                    if row_cnt >= X:
                        row_cnt = 1
                        row_num = board[i][j]
                    else:
                        can[i] = 0
                else:
                    can[i] = 0
            else:
                if board[i][j] == row_num - 1:
                    if row_cnt >= 0:
                        row_cnt = 1 - X
                        row_num = board[i][j]
                    else:
                        can[i] = 0
                else:
                    can[i] = 0
            if board[j][i] == col_num:
                col_cnt += 1
            elif board[j][i] > col_num:
                if board[j][i] == col_num + 1:
                    if col_cnt >= X:
                        col_cnt = 1
                        col_num = board[j][i]
                    else:
                        can[i + N] = 0
                else:
                    can[i + N] = 0
            else:
                if board[j][i] == col_num - 1:
                    if col_cnt >= 0:
                        col_cnt = 1 - X
                        col_num = board[j][i]
                    else:
                        can[i + N] = 0
                else:
                    can[i+N] = 0
        if row_cnt < 0:
            can[i] = 0
        if col_cnt < 0:
            can[i+N] = 0
    print('#{} {}'.format(tc, sum(can)))
