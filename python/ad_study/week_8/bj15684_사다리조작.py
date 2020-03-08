def run(cnt, l, start, numbers):
    global answer
    used.add((cnt, l, numbers))
    if answer != -1 and cnt >= answer: return
    if l == H + 1:
        if numbers == "".join([str(i) for i in range(N + 1)]):
            if answer == -1:
                answer = cnt
            elif answer > cnt:
                answer = cnt
        return
    if start == 1:
        for i in range(1, N):
            if i in lines[l]:
                numbers = numbers.replace(numbers[i:i+2], numbers[i+1:i-1:-1])
    run(cnt, l + 1, 1, numbers)
    for i in range(start, N):
        if cnt < 3 and not {i - 1, i, i + 1} & lines[l]:
            numbers = numbers.replace(numbers[i:i+2], numbers[i+1:i-1:-1])
            lines[l].add(i)
            if (cnt + 1, l, numbers) not in used:
                run(cnt + 1, l, i + 2, numbers)
            numbers = numbers.replace(numbers[i:i+2], numbers[i+1:i-1:-1])
            lines[l].remove(i)

answer = -1
N, M, H = map(int, input().split())
lines = {}
used = set()
for i in range(1, H + 1):
    lines[i] = set()
for _ in range(M):
    h, n = map(int, input().split())
    lines[h].add(n)
run(0, 1, 1, "".join([str(i) for i in range(N + 1)]))
print(answer)