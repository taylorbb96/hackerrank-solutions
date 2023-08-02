#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    total_swaps = 0

    for i in range(n):
        num_swaps = 0
        
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                num_swaps += 1
                total_swaps += 1
                
        if num_swaps == 0:
            break
        
    print(f'Array is sorted in {total_swaps} swaps.')
    print(f'First Element: {a.pop(0)}')
    print(f'Last Element: {a.pop()}')