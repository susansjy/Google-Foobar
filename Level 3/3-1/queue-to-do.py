#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:07:50 2023

@author: shenjiayi
"""
def test(start, length):
    # Your code here
    result = 0
    
    for i in range(length):
        for c in range(length - i):
            result ^= start + length*i + c
             
    return result
    


def solution(start, length):  
    result = 0
    
    for i in range(length):
        result ^= XOR_simplify(start + length*i, length-i)
             
    return result


def XOR_simplify(start, n):
    mod = n % 4
    if start % 2 == 0:
        if mod == 1:
            return start + n - 1
        elif mod == 2:
            return 1
        elif mod == 3:
            return start + n
        else:
            return 0
    else:
        if mod == 1:
            return start
        elif mod == 2:
            return start ^ (start + n - 1)
        elif mod == 3:
            return start - 1
        else:
            return (start - 1) ^ (start + n - 1)



if __name__ == '__main__':
    start = 5
    length = 10
    
    print(solution(start, length))
    print(test(start, length))
    
    
    
    
    
    
    
