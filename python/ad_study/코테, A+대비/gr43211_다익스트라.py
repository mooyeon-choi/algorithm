N, E = map(int, input().split())
node = [0xffffff]*(N+1)
values = []
for _ in range(E):
    values.append(tuple(map(int, input().split())))

values.sort(key=lambda x: x[2])
start = int(input())
node[start] = 0
for i in range(N - 1):
    for j in range(E):
        if node[values[j][0]] != 0xffffff or node[values[j][1]] != 0xffffff:
            if node[values[j][0]] + values[j][2] < node[values[j][1]]:
                node[values[j][1]] = node[values[j][0]] + values[j][2]
            elif node[values[j][1]] + values[j][2] < node[values[j][0]]:
                node[values[j][0]] = node[values[j][1]] + values[j][2]

for i in range(1, N + 1):
    print(f'{i}: {node[i]}')
