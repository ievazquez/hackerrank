#!/usr/bin/python3
# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    steps  = 0
    result = 0
    for i in range(len(s) ):
        steps += 1 if s[i] == 'U' else -1
        if steps == 0 and s[i] == 'U':
            result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

