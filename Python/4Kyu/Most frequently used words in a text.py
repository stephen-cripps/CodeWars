from collections import Counter
import imp
import re
test = imp.load_source('test', './test.py')

def top_3_words(input: str):
    stripped_input = re.sub("[^a-z' ]", " ", input.lower())
    split_input = stripped_input.split()
    filtered_input = filter(lambda x: re.search("[a-z]", x), split_input)
    counted_input = Counter(filtered_input)
    return list(map(lambda x : x[0], counted_input.most_common(3)))

test.assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
test.assert_equals(top_3_words("  , e   .. "), ["e"])
test.assert_equals(top_3_words("  ...  "), [])
test.assert_equals(top_3_words("  '  "), [])
test.assert_equals(top_3_words("  '''  "), [])
test.assert_equals(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])