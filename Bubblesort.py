#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    for each in range(len(a)):
        for every in range(len(a)-1):
            if a[every] > a[every + 1]:
                a[every], a[every + 1] = a[every + 1], a[every]
                swap_count += 1

    print(f'Array is sorted in {swap_count} swaps.')
    print(f'First Element: {first_num}')
    print(f'Last Element: {last_num}')




if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
