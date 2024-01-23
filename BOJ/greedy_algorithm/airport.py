# 공항
'''https://www.acmicpc.net/problem/10775'''

# Refer https://velog.io/@ich0906/%EB%B0%B1%EC%A4%80-10775-%EA%B3%B5%ED%95%AD

import sys

def find(g_i):
    if under_bounded[g_i] == g_i:
        return g_i
    under_bounded[g_i] = find(under_bounded[g_i])
    
    return under_bounded[g_i]

def search_gate(g_i):
    u_b = find(g_i)
    
    if not u_b:
        return False
    
    under_bounded[u_b] = find(u_b - 1)
    
    return True

if __name__ == "__main__":
    try:
        G, P = int(sys.stdin.readline()), int(sys.stdin.readline())  
        g = [int(sys.stdin.readline()) for _ in range(P)]
        
        under_bounded = [i for i in range(G+1)]

        answer = 0
        for g_i in g:
            
            if search_gate(g_i):
                answer += 1
            else:
                break
            
        print(answer)
            
            
        
        
    except ValueError or IndexError as e:
        print(e)
     