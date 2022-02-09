import imp
from typing import List
test = imp.load_source('test', './test.py')

def anagrams(word: str, words: List):
    sorted_word = sorted(word)
    return [x for x in words if sorted_word == sorted(x)]

test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])