def back(cnt):
    if cnt == 10:
        return



dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
board = [list(input()) for _ in range()]