import imp
test = imp.load_source('test', './test.py')

def century(year):
    return (year - 1)//100 + 1


test.assert_equals(century(1705), 18)
test.assert_equals(century(1900), 19)
test.assert_equals(century(1601), 17)
test.assert_equals(century(2000), 20)
test.assert_equals(century(356), 4)
test.assert_equals(century(89), 1)
