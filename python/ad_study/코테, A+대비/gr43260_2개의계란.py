number = int(input())
num, cnt = 0, 0
while num < number:
    cnt += 1
    num += cnt
print(cnt)