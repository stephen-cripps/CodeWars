import imp
test = imp.load_source('test', './test.py')

def count_positives_sum_negatives(arr):
    if(len(arr) == 0):
        return []
    return [len(list(filter(lambda value: value > 0, arr))),
            sum(list(filter(lambda value: value < 0, arr)))]


test.assert_equals(count_positives_sum_negatives(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]), [10, -65])
test.assert_equals(count_positives_sum_negatives(
    [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]), [8, -50])
test.assert_equals(count_positives_sum_negatives([1]), [1, 0])
test.assert_equals(count_positives_sum_negatives([-1]), [0, -1])
test.assert_equals(count_positives_sum_negatives(
    [0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0])
test.assert_equals(count_positives_sum_negatives([]), [])
