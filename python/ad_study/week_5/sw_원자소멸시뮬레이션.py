dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
atoms = {}

for tc in range(1, int(input()) + 1):
    answer = 0
    N = int(input())
    for i in range(N):
        x, y, d, K = map(int, input().split())
        atoms[i] = [x*2, y*2, d, K]
    for cnt in range(4000):
        visit = {}
        for i in range(N):
            if i in atoms:
                atoms[i][0] += dirs[atoms[i][2]][0]
                atoms[i][1] += dirs[atoms[i][2]][1]
                if -2000 > atoms[i][0] or 2000 < atoms[i][0] or -2000 > atoms[i][1] or 2000 < atoms[i][1]:
                    atoms.pop(i)
                    break
                if (atoms[i][0], atoms[i][1]) not in visit:
                    visit[(atoms[i][0], atoms[i][1])] = 1
                else:
                    visit[(atoms[i][0], atoms[i][1])] += 1
        for key, value in visit.items():
            if value > 1:
                for num in range(N):
                    if num in atoms:
                        if key == (atoms[num][0], atoms[num][1]):
                            answer += atoms[num][3]
                            atoms.pop(num)
    print('#{} {}'.format(tc, answer))