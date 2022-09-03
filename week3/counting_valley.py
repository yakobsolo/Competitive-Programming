#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

    
def countingValleys(steps, path):
    # Write your code here
    valleyCount = 0
    ground = 0
    for y in path:
        if y=="U":
            ground+=1
        else:
            ground-=1
        if ground==0 and x=="U":
            valleyCount+=1
    return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
