#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:27:30 2023

@author: shenjiayi
"""

def solution(n):
    options = [[0 for i in range(n+1)] for j in range(n+1)]
    
    options[0][0] = 1 # basic
        
    for prev in range(1, n+1):
        for remain in range(0, n+1):
            options[prev][remain] = options[prev-1][remain]  # add on the previous staircase
            if remain >= prev:  # build a new staircase
                options[prev][remain] += options[prev-1][remain-prev]
            
    
    return options[n][n] - 1

if __name__ == '__main__':        
    print(solution(200))