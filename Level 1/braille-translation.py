#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:51:22 2023

@author: shenjiayi
"""

def solution(s):
    letters = [ x for x in s ]
    output = [ '' for x in s ]
    print(output)
    
    braille_dic = {
        'a': '100000',
        'b': '110000',
        'c': '100100',
        'd': '100110',
        'e': '100010',
        'f': '110100',
        'g': '110110',
        'h': '110010',
        'i': '010100',
        'j': '010110',
        'k': '101000',
        'l': '111000',
        'm': '101100',
        'n': '101110',
        'o': '101010',
        'p': '111100',
        'q': '111110',
        'r': '111010',
        's': '011100',
        't': '011110',
        'u': '101001',
        'v': '111001',
        'w': '010111',
        'x': '101101',
        'y': '101111',
        'z': '101011',
        ' ': '000000'
    }
    

    for i in range(len(letters)):
        char = letters[i]
        initial = ''

        if char.isupper():
            initial = '000001'
            char = char.lower()
        
        output[i] = initial + braille_dic[char]

    return ''.join(output)


if __name__ == '__main__':
    assert solution('A') == '000001100000'
    
    print(solution(''))
    
    assert solution('B') == '000001110000'
    
    assert solution(' a A B') == '000000100000000000000001100000000000000001110000'
    
    assert solution(' T ') == '000000000001011110000000'
    
    assert solution('code') == '100100101010100110100010'

    assert solution('Braille') == '000001110000111010100000010100111000111000100010'

    assert solution('The quick brown fox jumps over the lazy dog') == '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'

