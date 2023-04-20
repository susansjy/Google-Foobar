#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:15:28 2023

@author: shenjiayi
"""

import numpy as np


def solution(src, dest):
    rows = 8
    cols = 8
    dis = 0
    
    # initialize chessboard
    chessboard = np.ones((3,3))
    chessboard = np.zeros((rows, cols), dtype = int)
    
    next_dic = {}
    
    for i in range(rows):
        for j in range(cols):
            chessboard[i][j] = 8 * i + j
            next_dic[chessboard[i][j]] = next_step_nums(chessboard[i][j])
    
    # find how many steps to take
    next_nums = [src]
     
    while dest not in next_nums:
        # keep finding if the dest can't be found in this step's nums
        next_nums = find_next_step(next_nums, next_dic)
        dis += 1
    
    return dis
    
        

def find_next_step(nodes, next_dic):
    """
    Return a list of possbile next nums for the current nodes
    """
    arr = []
    
    for n in nodes:
        arr.extend(next_dic[n])
    
    return arr


def next_step_nums(square):
    """
    Return a list of nums for next step
    """
    # locate src
    x = square // 8
    y = square % 8
    
    # calculate next step's possbile nums
    result = []
    next_nums = []
    if x >= 2:
        if y <= 6:
            result.append((x-2, y+1))
        if y >= 1:
            result.append((x-2, y-1))
    
    if x <= 5: 
        if y <= 6:
            result.append((x+2, y+1))
        if y >= 1:
            result.append((x+2, y-1))
    
    if x >= 1:
        if y <= 5:
            result.append((x-1, y+2))
        if y >= 2:       
            result.append((x-1, y-2))
            
    if x <= 6: 
        if y <= 5:
            result.append((x+1, y+2))
        if y >= 2:
            result.append((x+1, y-2))
            
    for i in range(len(result)):
        next_nums.append(8 * result[i][0] + result[i][1])
       
    return next_nums

    
if __name__ == '__main__':
    print(solution(0, 1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    