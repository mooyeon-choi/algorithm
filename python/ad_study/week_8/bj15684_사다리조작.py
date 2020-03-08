def back(cnt, line):
    if cnt == 3 or line == M:
        return



answer = -1
N, M, H = map(int, input().split())
lines = {}
if M:
    for _ in range(M):
        h, n = map(int, input().split())
        if h not in lines:
            lines[h] = [n]
        else:
            lines[h].append(n)

if lines:
