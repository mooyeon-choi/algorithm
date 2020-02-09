A, B = map(int, input().split())
N, M = map(int, input().split())
board = [[0]*B for _ in range(A)]
robots = {}
dirs = ['E', 'S', 'W', 'N']
for i in range(1, N + 1):
    x, y, k = list(input().split())
    robots[str(i)] = [int(y) - 1, int(x) - 1, k]
    board[int(y) - 1][int(x) - 1] = i
for _ in range(M):
    num, run, cnt = input().split()
    cnt = int(cnt)
    board[robots[num][0]][robots[num][1]] = 0
    if run == 'F':
        if robots[num][2] == 'E':
            for __ in range(cnt):
                robots[num][1] += 1
                if board[robots[num][0]][robots[num][1]]:
                    
        elif robots[num][2] == 'S':
            pass
        elif robots[num][2] == 'W':
            pass
        else:

    else:
        for i in range(4):
            if dirs[i] == run:
                idx = i
                break
        if run == 'L':
            robots[num][2] = dirs[(idx - cnt) // 4]
        else:
            robots[num][2] = dirs[(idx + cnt) // 4]
