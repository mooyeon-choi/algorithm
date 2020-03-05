def DFS(num, idx):
    for i in range(idx, N):
        if num + nums[i] not in scores:
            scores.add(num + nums[idx])
            DFS(num + nums[idx], i + 1)


for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    scores = set({0})
    for i in range(N):
        DFS(0, i)
    print(f'#{tc} {len(scores)}')