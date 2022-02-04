import imp
test = imp.load_source('test', './test.py')


def solution(s):
    out = []
    padded = s + "_"
    for x in range(0, len(s), 2):
        out.append(padded[x] + (padded[x+1]))
    
    return out


tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
