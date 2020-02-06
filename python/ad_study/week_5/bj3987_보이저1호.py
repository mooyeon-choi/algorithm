import sys
sys.setrecursionlimit(100000)

def slash(i, j, k, idx, cnt):
    global answer, answer_idx
    if (i, j, k) not in visit:
        visit.append((i, j, k))
    else:
        answer = 'Voyager'
        answer_idx = idx
        return
    if k == 0:
        run(i, j + 1, 1, idx, cnt + 1)
    elif k == 1:
        run(i - 1, j, 0, idx, cnt + 1)
    elif k == 2:
        run(i, j - 1, 3, idx, cnt + 1)
    else:
        run(i + 1, j, 2, idx, cnt + 1)


def reverse_slach(i, j, k, idx, cnt):
    global answer, answer_idx
    if (i, j, k) not in visit:
        visit.append((i, j, k))
    else:
        answer = 'Voyager'
        answer_idx = idx
        return
    if k == 0:
        run(i, j - 1, 3, idx, cnt + 1)
    elif k == 1:
        run(i + 1, j, 2, idx, cnt + 1)
    elif k == 2:
        run(i, j + 1, 1, idx, cnt + 1)
    else:
        run(i - 1, j, 0, idx, cnt + 1)


def run(i, j, k, idx, cnt):
    global answer, answer_idx
    if 0 > i or N <= i or 0 > j or M <= j:
        if answer < cnt:
            answer = cnt
            answer_idx = idx
        return
    while board[i][j] == '.':
        i += dirs[k][0]
        j += dirs[k][1]
        cnt += 1
        if 0 > i or N <= i or 0 > j or M <= j:
            if answer < cnt:
                answer = cnt
                answer_idx = idx
            return
    if board[i][j] == '/':
        slash(i, j, k, idx, cnt)
    elif board[i][j] == '\\':
        reverse_slach(i, j, k, idx, cnt)
    else:
        if answer < cnt:
            answer = cnt
            answer_idx = idx
        return


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
R, C = map(int, input().split())
answer = 0
answer_idx = 0
for i in range(4):
    if answer == 'Voyager':
        break
    visit = []
    run(R - 1, C - 1, i, i, 0)

d = ['U', 'R', 'D', 'L']
print(d[answer_idx])
print(answer)
