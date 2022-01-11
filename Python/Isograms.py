def is_isogram(input):
    input = input.lower()
    stack = ""

    for character in input:
        if stack.find(character) == -1:
            stack += character
        else:
            return False

    return True

assert is_isogram("Dermatoglyphics") == True
assert is_isogram("isogram") == True
assert is_isogram("aba") == False
assert is_isogram("moOse") == False
assert is_isogram("isIsogram") == False
assert is_isogram("") == True