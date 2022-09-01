#!/bin/python3

import math
import os
import random
import re
import sys


# The function accepts INTEGER_ARRAY arr as parameter.
# La función recibe un Array y calcula el ratio de valores positivos, negativos e iguales a cero
# se limita el posicionamiento decimal a 5 uns

pos=[]
neg=[]
zero=[]

def plusMinus(arr):
    for element in arr:
        #print(element)
        
        if element>0:
            pos.append(element)
        elif element<0:
            neg.append(element)
        else:
            zero.append(element)
    # Write your code here
    
    rpos=len(pos)/len(arr)
    rneg=len(neg)/len(arr)
    rzero=len(zero)/len(arr)
    
    result=[rpos,rneg,rzero]
    #result=np.array(result)
    for i in result: print('%.5f' % i, end = "\n")
    return()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
