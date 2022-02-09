from ast import If
import imp
import string
test = imp.load_source('test', './test.py')


def is_int(input: str):
    try:
        int(input)
        return True
    except ValueError:
        return False


def increment_string(input: str):

    if not input:
        return "1"

    last = input[-1]
    if not is_int(input[-1]):
        return input + "1"

    num = last

    for i in range(len(input) - 1):
        char = input[-i-2]
        if is_int(char):
            num = char + num
        else:
            incremented = str(int(num) + 1).zfill(len(num))
            return input.replace(num, incremented)

    return str(int(num) + 1).zfill(len(num))


# test.assert_equals(increment_string("foo"), "foo1")
# test.assert_equals(increment_string("foobar001"), "foobar002")
# test.assert_equals(increment_string("foobar1"), "foobar2")
# test.assert_equals(increment_string("foobar00"), "foobar01")
# test.assert_equals(increment_string("foobar99"), "foobar100")
# test.assert_equals(increment_string("foobar099"), "foobar100")
test.assert_equals(increment_string("099"), "100")
test.assert_equals(increment_string(""), "1")
