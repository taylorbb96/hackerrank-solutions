#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bin_n = bin(n)[2:]
    
    max_consecutive_1s = 0
    consecutive_1s = 0
    
    for digit in bin_n:
        if digit == '1':
            consecutive_1s += 1
        else:
            if consecutive_1s > max_consecutive_1s:
                max_consecutive_1s = consecutive_1s
            consecutive_1s = 0

    if consecutive_1s > max_consecutive_1s:
        max_consecutive_1s = consecutive_1s
                
    print(max_consecutive_1s)
