def solution(begin, end):
    answer = []
    for num in range(begin, end+1):
        for i in range(2, int(num**(1/2))+1):
            if not num % i:
                answer.append(num//i)
                break
        else:
            if num == 1:
                answer.append(0)
            else:
                answer.append(1)
    return answer