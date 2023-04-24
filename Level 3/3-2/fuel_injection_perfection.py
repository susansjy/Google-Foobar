# -*- coding: utf-8 -*-
"""
Fuel Injection Perfection
"""

def solution(n):
    n = int(n)
    
    step = 0
    while n != 1:
        if n == 3:
            return step + 2
        else:
            if n % 2 == 0:  # n is even
                n //= 2
            else:           # n is odd
                if (n // 2) % 2 == 0:  # quotient is even
                    n -= 1
                else:                  # quotient is odd
                    n += 1
        step += 1
        
    return step
            
    
if __name__ == '__main__':
    print(solution('6'))
    
    