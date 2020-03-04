def back(cnt, numsum):
    global answer
    if cnt == N:
        if answer < numsum:
            answer = numsum
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            back(cnt + 1, numsum * (person[cnt][i] / 100))
            used[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    answer = 0
    person = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*N
    back(0, 1)
    print(f'#{tc} {round(answer * 100, 6):0.6f}')
