t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    number = set([0])
    for i in range(n):
        for j in number:
            number.add(j+numbers[i])
    print(number)
    print('#{} {}'.format(tc, len(number)))