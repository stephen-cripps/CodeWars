import imp
test = imp.load_source('test', './test.py')  

def greet(name):
    return "Hello, %s how are you doing today?"%name
      
test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")