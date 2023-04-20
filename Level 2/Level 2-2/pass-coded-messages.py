#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:13:00 2023

@author: shenjiayi
"""

def solution(l):
    if len(l) == 0:
        return 0
    
    l.sort(reverse=True)
    
    if sum(l) % 3 == 0:
        return to_digit(l)
    else:
        i = len(l) - 1
        
        while i > 0 and (sum(l) - l[i]) % 3 != 0:
            i -= 1

        if i > 0:
            l.pop(i)
            return to_digit(l)
        else:
            l.pop()
            return solution(l)

def to_digit(l):
    n = 0
    
    for i in range(len(l)):
        n += l[i] * 10 ** (len(l) - i - 1)

    return n
    
    
if __name__ == '__main__':
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
    print(solution([3, 1, 4, 1, 9, 2, 5, 7]))
    print(solution([0, 1, 1, 3, 2]))
    print(solution([0, 1, 3, 2]))