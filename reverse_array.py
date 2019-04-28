#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a,arr_count):
    rev = [a.pop() for i in range(0,arr_count)]
    return rev

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr,arr_count)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
