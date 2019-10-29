#!/usr/bin/env python3

# Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118] on linux

# a narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits
# 153 = 1**3 + 5**3 + 3**3 -> True

def main(a):
    y = 0 ; str_a = str(a)
    for i in range(len(str_a)):
        y += int(str_a[i]) ** len(str_a)
    return True if a == y else False

def inpt():
    a = int(input("number: "))
    print(main(a))

inpt()
