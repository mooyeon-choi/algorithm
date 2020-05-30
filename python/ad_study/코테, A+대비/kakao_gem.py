gems = ['a', 'b', 'b', 'a', 'b', 'b', 'b', 'c']

{'a': 3, 'b': 1, 'c': -1}
def solution(gems):
    gem_set = set(gems)
    answer = 0xfffffff
    min_gem = 'a'
    gem_dict = {}
    for gem in gem_set:
        gem_dict[gem] = -1

    for idx, gem in enumerate(gems):
        gem_dict[gem] = idx
        if gem == min_gem:
            min_value = 0xffff
            for g in gem_set:
                if gem_dict[g] < min_value:
                    min_value = gem_dict[g]
                    min_gem = g
            if min(gem_dict.values()) != -1:
                length = idx - gem_dict[min_gem] + 1
                if length < answer:
                    answer = length
    return answer

print(solution(gems))