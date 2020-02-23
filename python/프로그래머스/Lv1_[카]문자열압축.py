def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        length = i
        before = s[:i]
        used = 0
        for j in range(i, len(s), i):
            if before == s[j:j+i]:
                if not used:
                    length += 1
                    used = 1
            else:
                if j+i >= len(s):
                    length += len(s) - j
                else:
                    length += i
                    before = s[j:j+i]
                    used = 0
        if answer > length:
            answer = length
    return answer