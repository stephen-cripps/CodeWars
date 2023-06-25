import imp
test = imp.load_source('test', './test.py')

def merge_overlapping_intervals(intervals):
    merged = []
    mergedIndexes = []
    i=0
    for intervalA in intervals:
        if i in mergedIndexes:
            continue
        j=i+1
        for intervalB in intervals[i+1:]:
            if (intervalA[0] >= intervalB[0] and intervalA[0]<= intervalB[1]) or (intervalB[0] >= intervalA[0] and intervalB[0]<= intervalA[1]):
                intervalA = (min(intervalA[0],intervalB[0]) max(intervalA[1],intervalB[1]))
                mergedIndexes.append(j)

            j+=1
        merged.append(intervalA)
        i+=1

    return merged

    

def sum_of_intervals(intervals):
    intervals = merge_overlapping_intervals(intervals)
    return sum([interval[1]-interval[0] for interval in intervals])
   
# test.assert_equals(sum_of_intervals([(1, 5)]), 4)
# test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
# test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
# test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5), (2,6), (1, 4)]), 8)