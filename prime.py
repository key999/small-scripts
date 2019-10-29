#!/usr/bin/env python3

# Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118] on linux

# checks if a number is prime or not

def main(n):
    if n == 2:
        return True
    elif n < 2:
        return None
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        else:
            return True

def inpt():
    n = int(input("number: "))
    print(main(n))

inpt()
