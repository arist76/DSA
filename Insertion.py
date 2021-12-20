#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    def iter_print():
        temp_str = ''
        for every in arr:
            temp_str += f'{every} '
        temp_str = temp_str.strip()
        print(temp_str)
        temp_str = ''

    temp = arr[n-1]
    for each in reversed(arr):
        if each >= temp:
            try:
                if arr.index(each) == 0:
                    arr[1] = each
                    iter_print()
                    arr[0] = temp
                    iter_print()
                    break
                else:
                    arr[arr.index(each) + 1] = each
                    iter_print()
                    continue
            except:
                pass
        elif each <= temp:                
            arr[arr.index(each) + 1] = temp
            iter_print()
            break
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
