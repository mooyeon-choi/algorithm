import collections as col

def BFS():
    if N == 0:
        return 0
    que = col.deque('0')
    cnt = 0
    while True:
        num = que.popleft()
        for i in range(10):
            if num == 0:
                cnt += 1
                if cnt == N:
                    return int(f'{num}{i}')
                que.append(str(int(f'{num}{i}')))
            else:
                for 
N = int(input())

print(number)
