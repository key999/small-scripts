#!/usr/bin/env python3

# Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
# [GCC 6.3.0 20170118] on linux

# calculates the change
# takes input in cents or whatever (basically *100)
# returns a tuple with lists of dollars and cents separately

def main(price, money_given):
    change = money_given - price
    coins = (50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
    W = [] ; Y = [] ; i = 0
    while change > 0:
        while i <= 14:
            if coins[i] <= change:
                change -= coins[i]
                W.append(coins[i])
            else:
                i += 1
    else:
        for i in W:
            if i < 100:
                Y.append(i)
                W.remove(i)
    for i in range(len(W)):
        W[i] = W[i] // 100
    X = (W, Y)
    return(X)
