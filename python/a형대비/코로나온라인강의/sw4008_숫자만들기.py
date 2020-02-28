def DFS(num, cnt):
    global maxnum, minnum
    if cnt == N:
        if num > maxnum:
            maxnum = num
        if num < minnum:
            minnum = num
        return
    for i in range(len(sign)):
        if sign[i]:
            sign[i] -= 1
            DFS(int(eval(str(num) + signlist[i] + numbers[cnt])), cnt + 1)
            sign[i] += 1


signlist = ['+', '-', '*', '/']
for tc in range(1, int(input()) + 1):
    minnum = 0xffffff
    maxnum = -0xffffff
    N = int(input())
    sign = list(map(int, input().split()))
    numbers = list(input().split())
    DFS(int(numbers[0]), 1)
    print(f'#{tc} {maxnum - minnum}')