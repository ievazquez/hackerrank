#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = {}
    for i in ar:
        count[i] = count.get(i,0) + 1
    newDict = dict(filter(lambda elem: elem[1] >= 2, count.items()))
    result = 0
    for i in newDict:
        result +=  int(newDict[i] / 2)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
