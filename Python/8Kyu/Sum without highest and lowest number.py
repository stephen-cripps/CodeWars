import imp
from operator import truediv
test = imp.load_source('test', './test.py')  

def sum_array(arr):
    if not arr or len(arr) == 1:
        return 0
    arr.sort()
    return sum(arr[1:-1])

test.assert_equals(sum_array(None), 0)
test.assert_equals(sum_array([]), 0)
test.assert_equals(sum_array([3]), 0)
test.assert_equals(sum_array([-3]), 0)
test.assert_equals(sum_array([ 3, 5]), 0)
test.assert_equals(sum_array([-3, -5]), 0)
test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)