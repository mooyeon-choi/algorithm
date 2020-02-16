for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    nums = input()
    result = []
    for i in range(N//4):
        for j in range(4):
            num_str = ''
            for k in range(N//4):
                num_str += nums[(j*N//4 + i + k) % N]
            if num_str not in result:
                result.append(num_str)
    result.sort(reverse=True)
    print('#{} {}'.format(tc, int(result[K - 1], 16)))
