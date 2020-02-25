def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        length = i
        before = s[:i]
        used = 0
        for j in range(i, len(s), i):
            if before == s[j:j+i]:
                used += 1
            else:
                if used:
                    length += len(str(used+1))
                length += len(s[j:j+i])
                before = s[j:j+i]
                used = 0
        if used:
            length += len(str(used+1))
        if answer > length:
            answer = length
    return answer