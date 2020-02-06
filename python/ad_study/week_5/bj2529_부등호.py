def DFS(num, cnt):
    global low_num, high_num
    if cnt > K:
        if int(num) < int(low_num):
            low_num = num
        if int(num) > int(high_num):
            high_num = num
        return
    if not cnt:
        for i in range(10):
            if not used[i]:
                used[i] = 1
                DFS(num + str(i), cnt + 1)
                used[i] = 0
    else:
        for i in range(10):
            if mark[cnt - 1] == '>':
                if int(num[-1]) > i and not used[i]:
                    used[i] = 1
                    DFS(num + str(i), cnt + 1)
                    used[i] = 0
            else:
                if int(num[-1]) < i and not used[i]:
                    used[i] = 1
                    DFS(num + str(i), cnt + 1)
                    used[i] = 0

K = int(input())
mark = list(map(str, input().split()))
used = [0]*10
low_num = '9999999999'
high_num = '0'
DFS('', 0)
print(high_num)
print(low_num)
