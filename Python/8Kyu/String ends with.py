def solution(string, ending):
    return string[-len(ending):] == ending or ending == ''

assert solution('abcde', 'cde')
assert not solution('abcde', 'abc')
assert solution('abcde', '')