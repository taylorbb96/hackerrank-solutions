#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split()
    capped_words = []
    
    for word in words:
        capped_words.append(word[0].capitalize() + word[1:])
    
    return ' '.join(capped_words)

if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result + '\n')