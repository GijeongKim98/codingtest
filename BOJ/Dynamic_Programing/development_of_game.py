# 게임 개발
'''https://www.acmicpc.net/problem/1516'''

import sys
from collections import deque

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        buildings = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        graph = {building:[] for building in range(1,N+1)}
        times = [0]
        in_degree_list = [0 for _ in range(N+1)]
        
        start_nodes = []
        
        for idx, info in enumerate(buildings):
            times.append(info[0])
            in_degree_list[idx+1] = len(info) - 2
            for idx2 in info[1:-1]:
                graph[idx2].append(idx+1)
            
            if in_degree_list[idx+1] == 0:
                start_nodes.append(idx+1)
        
        queue = deque(start_nodes)
        rlt = [0 for _ in range(N+1)]
        for s_n in start_nodes:
            rlt[s_n] = times[s_n]
        
        while queue:
            pop = queue.popleft()
            for new in graph[pop]:
                in_degree_list[new] -= 1
                rlt[new] = max(rlt[new], rlt[pop]+times[new])
                if not in_degree_list[new]:
                    queue.append(new)
        
        print(*rlt[1:],sep="\n")

    except ValueError or IndexError as e:
        print(e)