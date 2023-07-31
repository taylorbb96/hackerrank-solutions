#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglass_sum_max = None
    
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass_sum = top + mid + bot
            
            if i == 0 and j == 0:
                hourglass_sum_max = hourglass_sum
            if hourglass_sum > hourglass_sum_max:
                hourglass_sum_max = hourglass_sum
    
    print(hourglass_sum_max)