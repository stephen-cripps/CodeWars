import imp
test = imp.load_source('test', './test.py')

def high_and_low(numbers):
    numSorted = sorted(map(lambda num: int(num), numbers.split(" ")))
    return f"{numSorted[-1]} {numSorted[0]}"


test.assert_equals(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")
test.assert_equals(high_and_low("1 2 3"), "3 1")