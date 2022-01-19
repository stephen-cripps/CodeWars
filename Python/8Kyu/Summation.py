def summation(num):
    res = 0
    
    for i in range (num):
        res += i+1

    return res

assert summation(1) == 1
assert summation(8) == 36
assert summation(22) == 253
assert summation(100) == 5050
assert summation(213) == 22791