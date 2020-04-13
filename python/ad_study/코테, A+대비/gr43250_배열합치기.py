A, B = map(int, input().split())
result = sorted(list(map(int, input().split())) + list(map(int, input().split())))
answer = ''
for num in result: answer += str(num) + ' '
print(answer)