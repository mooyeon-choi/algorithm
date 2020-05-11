num_list = []
for _ in range(int(input())):
    num_list.append(list(map(int, input().split())))

for i in range(len(num_list) - 1, 0, -1):
    for j in range(len(num_list[i]) - 1):
        num_list[i-1][j] += max(num_list[i][j], num_list[i][j+1])

print(num_list[0][0])