# 개미굴
'''https://www.acmicpc.net/problem/14725'''

import sys

P = "--"

try:
    N = int(sys.stdin.readline())

    repo_infos = []
    
    word_set = set()
    
    for _ in range(N):
        repo_info = sys.stdin.readline().rstrip().split(" ")
        repo_info[0] = int(repo_info[0])
        
        word_set = word_set.union(set(repo_info[1:]))
        
        repo_info = repo_info + [0] * (16 - len(repo_info))
        
        repo_infos.append(repo_info)
    
    word_dict = {val : idx for idx, val in enumerate(sorted(list(word_set)))}
    word_dict[0] = len(word_dict)
    
    repo_infos.sort(key=lambda x : x[0], reverse=True)
    
    for idx in range(15, 0, -1):
        repo_infos.sort(key=lambda x: word_dict[x[idx]])
    
    
    for r_idx, repo in enumerate(repo_infos):
        c = 0
        for idx, value in enumerate(repo[1:]):
            if not value:
                break
            
            if r_idx == 0:
                print(P*idx+value)
                continue
            
            if c or repo_infos[r_idx-1][idx+1] != value:
                c = 1
                print(P*idx+value)
        
except ValueError or IndexError as e:
    print(e)