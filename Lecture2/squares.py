#references function  in functions.py -> this is a module

import functions
for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
