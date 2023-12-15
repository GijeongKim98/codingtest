# 1의 개수 세기
'''https://www.acmicpc.net/problem/9527'''

import math

def count_1(num):
    q, r, k = num // 2, num % 2, 0
    
    bits = []
    
    while q > 0 or r > 0:
        bits.append(r)
        q, r = q//2, q%2
        
    # print(bits)
    
    len_bits = len(bits)
    result = 0
    pre_count = 0
    
    for k in range(len_bits-1,-1,-1):
        if bits[k]:
            result += counts[k]
            result += constants[k] * pre_count
            pre_count += 1
    
    return result, pre_count
    

if __name__ == "__main__":
    try: 
        A, B = map(int, input().split(" "))

        n = int(math.log(B, 2))
        
        counts = [0,1]
        constants = [1,2]
        
        for i in range(2, n+1):
            next_count = counts[-1] * 2 + constants[-1]
            constants.append(constants[-1]*2)
            counts.append(next_count)
            
        counts = list(map(lambda x:x+1, counts))
        
        # print(f"counts = {counts}")
        # print(f"constants = {constants}")
        
        
        # 1 ~ A 까지의 1의 개수 a, 1 ~ B 까지의 1의 개수 b
        # We solve b - a

        a, a_ = count_1(A)
        b, _ = count_1(B)
        
        a = a - a_
        
        print(b-a)
        
    except ValueError or IndexError as e:
        print(e)