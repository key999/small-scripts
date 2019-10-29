#!/usr/bin/env python3

# Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118] on linux

def fibo(n):
    W = [1, 1]
    for i in range(n):
        W.append(W[i] + W[i+1])
    return(W)

def inpt():
    n = int(input("steps: "))
    print(fibo(n))

inpt()
