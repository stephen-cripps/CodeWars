import imp
test = imp.load_source('test', './test.py')

def find_it(seq):
    unique = set(seq)

    for n in unique:
        if(seq.count(n) % 2 == 1):
            return n


test.assert_equals(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
test.assert_equals(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)
test.assert_equals(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)
test.assert_equals(find_it([10]), 10)
test.assert_equals(find_it([10, 10, 10]), 10)
test.assert_equals(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)
test.assert_equals(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)
