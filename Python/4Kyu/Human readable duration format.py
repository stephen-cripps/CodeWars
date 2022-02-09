import imp
test = imp.load_source('test', './test.py')


def append_value(output_list, value, baseString):

    if value == 0:
        return
    if value == 1:
        output_list.insert(0, f"{value} {baseString}")
    elif value > 1:
        output_list.insert(0, f"{value} {baseString}s")

    if len(output_list) == 2:
        output_list.insert(1, " and ")
    elif len(output_list) > 2:
        output_list.insert(1, ", ")


def format_duration(input: int):
    if not input:
        return "now"

    output_list = []

    seconds = input % 60
    append_value(output_list, seconds, "second")

    input //= 60
    minutes = input % 60
    append_value(output_list, minutes, "minute")

    input //= 60
    hours = input % 24
    append_value(output_list, hours, "hour")

    input //= 24
    days = input % 365
    append_value(output_list, days, "day")

    input //= 365
    append_value(output_list, input, "year")

    return "".join(output_list)


test.assert_equals(format_duration(""), "now")
test.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
test.assert_equals(format_duration(31622400 + 3662),
                   "1 year, 1 day, 1 hour, 1 minute and 2 seconds")
