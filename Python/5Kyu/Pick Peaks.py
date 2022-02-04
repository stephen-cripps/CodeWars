import imp
test = imp.load_source('test', './test.py')


def is_peak(arr, i):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        return True
    if arr[i] <= arr[i-1] or arr[i] < arr[i+1]:
        return False

    # If we've got here, we need to check if the index is the start of a plateau
    x = 2
    while True:
        if i+x == len(arr) or arr[i] < arr[i+x]:
            return False
        if arr[i] > arr[i+x]:
            return True
        x += 1

def pick_peaks(arr):
    positions = []
    peaks = []
    for i in range(1, len(arr)-1):
        if is_peak(arr, i):
            positions.append(i)
            peaks.append(arr[i])

    return {"pos": positions, "peaks": peaks}


test.assert_equals(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {
                   "pos": [3, 7], "peaks": [6, 3]})
test.assert_equals(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {
                   "pos": [3, 7], "peaks": [6, 3]})
test.assert_equals(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {
                   "pos": [3, 7, 10], "peaks": [6, 3, 2]})
test.assert_equals(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {
                   "pos": [2, 4], "peaks": [3, 2]})
test.assert_equals(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {
                   "pos": [2], "peaks": [3]})
test.assert_equals(pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]), {
                   "pos": [2], "peaks": [3]})
test.assert_equals(pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]), {
                   "pos": [2], "peaks": [3]})
test.assert_equals(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]), {
                   "pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]})
test.assert_equals(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4,
                   8, 13, 9, 16, 18, 6, 7]), {'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})
test.assert_equals(pick_peaks([]), {"pos": [], "peaks": []})
test.assert_equals(pick_peaks([1, 1, 1, 1]), {"pos": [], "peaks": []})
test.assert_equals(pick_peaks([1, 1, 2, 2]), {"pos": [], "peaks": []})

