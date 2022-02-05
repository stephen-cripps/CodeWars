import imp
test = imp.load_source('test', './test.py')



def find_missing(sequence: list):
    step = min({sequence[1]-sequence[0], sequence[2]-sequence[1], sequence[3]-sequence[2]})
    for i, n in enumerate(sequence):
        if n + step != sequence[i+1]:
            return n+step

    return sequence[0]




test.assert_equals(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
test.assert_equals(find_missing([1, 3, 4, 5, 6, 7, 8, 9]), 2)