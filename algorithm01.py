for tc in range(10):
    n = int(input())
    b_list = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        max_value = b_list[i-2]
        for j in range(-1, 3):
            if j == 0: continue
            if b_list[i+j] > max_value:
                max_value = b_list[i+j]
        if b_list[i] > max_value:
            result += b_list[i] - max_value
    print('#{} {}'.format(tc+1, result))