#!/usr/bin/env python3

# Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118] on linux

def main(n):
    if n == 1 or n == 2:
        return(n)
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return(fact)

def inpt():
    n = int(input("number: "))
    print(main(n))

inpt()
