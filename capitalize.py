'''Note::
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, rohit sharma should be capitalised correctly as Rohit Sharma.
Sample Input::
    rohit sharma
Sample Output::
    Rohit Sharma
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a_string = s.split(' ') 
    return (' '.join((word.capitalize() for word in a_string))) 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

