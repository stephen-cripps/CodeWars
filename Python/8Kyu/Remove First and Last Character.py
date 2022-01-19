import imp
test = imp.load_source('test', './test.py')

def remove_char(s):
    return s[1:-1]
    # your code here


test.assert_equals(remove_char('eloquent'), 'loquen')
test.assert_equals(remove_char('country'), 'ountr')
test.assert_equals(remove_char('person'), 'erso')
test.assert_equals(remove_char('place'), 'lac')
test.assert_equals(remove_char('ok'), '')
test.assert_equals(remove_char('ooopsss'), 'oopss')
