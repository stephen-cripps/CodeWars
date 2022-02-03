import imp
test = imp.load_source('test', './test.py')


def paperwork(n, m):
    if(n < 0 or m < 0):
        return 0

    return n*m


test.assert_equals(paperwork(5, 5), 25, "Failed at Paperwork(5,5)")
test.assert_equals(paperwork(-5, 5), 0, "Failed at Paperwork(-5,5)")
test.assert_equals(paperwork(5, -5), 0, "Failed at Paperwork(5,-5)")
test.assert_equals(paperwork(-5, -5), 0, "Failed at Paperwork(-5,-5)")
test.assert_equals(paperwork(5, 0), 0, "Failed at Paperwork(5,0)")
