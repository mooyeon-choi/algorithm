def breeding(cell_list):
    new_cell = set()
    for i, j in cell_list:
        for k in range(4):
            if (i+dirs[k][0], j+dirs[k][1]) not in visit:
                visit.add((i+dirs[k][0], j+dirs[k][1]))
                new_cell.add((i+dirs[k][0], j+dirs[k][1]))
    return new_cell


dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cell = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set(), 10: set()}
    active_cell = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set(), 10: set()}
    visit = set()
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                cell[board[i][j]].add((i, j))
                visit.add((i, j))
    for turn in range(1, K+1):
        for num in range(10, 0, -1):
            if not turn % (num + 1):
                if cell[num]:
                    active_cell[num] = cell[num]
                    cell[num] = breeding(cell[num])
            if not (turn + 2) % (num + 1):
                if active_cell[num]:
                    active_cell[num] = set()
    answer = sum([len(cell[i] | active_cell[i]) for i in range(1, 11)])
    print('#{} {}'.format(tc, answer))