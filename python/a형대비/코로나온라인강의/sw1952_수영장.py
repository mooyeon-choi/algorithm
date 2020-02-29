def back(cnt, total):
    global answer
    if total > answer:
        return
    if cnt >= 12:
        answer = total
        return
    if attendance[cnt]:
        for i in range(2, 0, -1):
            if i < 2:
                if attendance[cnt] * payment[0] < payment[1]:
                    back(cnt + 1, total + attendance[cnt] * payment[0])
                else:
                    back(cnt + 1, total + payment[1])
            else:
                back(cnt + 3, total + payment[i])
    else:
        back(cnt + 1, total)


for tc in range(1, int(input()) + 1):
    payment = list(map(int, input().split()))
    attendance = list(map(int, input().split()))
    answer = payment[-1]
    back(0, 0)
    print(f'#{tc} {answer}')