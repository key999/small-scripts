#!/usr/bin/env python3

# Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118] on linux

# Levenshtein distance is a string metric for measuring the difference between two sequences.
# Informally, the Levenshtein distance between two words is the minimum number
# of single-character edits required to change one word into the other. 

def main(a, b):
    count = 0
    if len(a) != len(b):
        if len(b) > len(a):
            length = len(a)
        else:
            length = len(b)
        count = abs(len(a) - len(b))
        for i in range(length):
            if a[i] == b[i]:
                pass
            else:
                count +=1
        return(count)
    else:
        for i in range(len(a)):
            if a[i] == b[i]:
                pass
            else:
                count += 1
        return(count)

def inpt():
    a = input(" first string - ")
    b = input("second string - ")
    print("leve =", main(a, b))

inpt()
