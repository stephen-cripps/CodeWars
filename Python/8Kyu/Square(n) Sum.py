import imp
test = imp.load_source('test', './test.py')  

def square_sum(numbers):
    tot = 0
    for n in numbers:
        tot += n**2
    return tot

test.assert_equals(square_sum([1,2]), 5)
test.assert_equals(square_sum([0, 3, 4, 5]), 50)
test.assert_equals(square_sum([]), 0)
test.assert_equals(square_sum([-1,-2]), 5)
test.assert_equals(square_sum([-1,0,1]), 2)