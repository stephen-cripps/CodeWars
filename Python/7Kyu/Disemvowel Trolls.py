import imp
test = imp.load_source('test', './test.py')  

def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        string_ = string_.replace(vowel, "")
        string_ = string_.replace(vowel.upper(), "")
    return string_

test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")