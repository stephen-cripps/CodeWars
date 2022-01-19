import imp
test = imp.load_source('test', './test.py')  

def make_upper_case(s):
    return s.upper()

test.assert_equals(make_upper_case("hello"), "HELLO")