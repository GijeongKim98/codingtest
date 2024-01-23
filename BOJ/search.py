# 찾기
'''https://www.acmicpc.net/problem/1786'''

import sys

def get_next():
    res = [-1] * len_p
    
    j = -1
    for i in range(len_p):
        res[i] = j
        while j >= 0 and pattern[i] != pattern[j]:
            j = res[j]
        j += 1
    
    res2 = res[:]
    
    for idx, next in enumerate(res[1:], start=1):
        if pattern[idx] == pattern[next]:
            res[idx] = res[next]
    
    return res, res2

if __name__ == "__main__":
    try:
        string = sys.stdin.readline().rstrip("\n")
        pattern = sys.stdin.readline().rstrip("\n")
        
        len_s, len_p = len(string), len(pattern)
        
        nexts, next2 = get_next()
        
        # print(nexts)
        
        p_idx = 0
        
        answer = []
        
        pattern += "-"
        
        for s_idx, s in enumerate(string):
            while p_idx >= 0 and s != pattern[p_idx]:
                p_idx = nexts[p_idx]
            
            if p_idx + 1 == len_p:
                p_idx = next2[p_idx] # todo
                while p_idx >= 0 and s != pattern[p_idx]:
                    p_idx = next2[p_idx]
                answer.append(s_idx - len_p + 2)
            
            p_idx += 1
            
            
        print(len(answer))
        if answer:
            print(*answer, sep=" ")
    
    except IndexError as e:
        print(e)
        