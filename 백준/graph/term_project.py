# 텀 프로젝트
'''https://www.acmicpc.net/problem/9466'''

'''import sys
from collections import deque

if __name__ == "__main__":
    try:
        T = int(sys.stdin.readline())
        answer = []
        for _ in range(T):
            n = int(sys.stdin.readline())
            graph = [0] + list(map(int, sys.stdin.readline().split(" ")))
            visited = [0 for _ in range(n+1)]
            set1, set2 = set(), set()
            
            for idx in range(1, n+1):
                if visited[idx]:
                    continue
            
                visited[idx] = 1
                queue = deque([idx])
                
                while not visited[graph[idx]]:
                    idx = graph[idx]
                    visited[idx] = 1
                    queue.append(idx)

                node = graph[idx]
                
                if node in set1 or node in set2:
                    set1 = set1.union(set(queue))
                    continue
                
                while queue and node != queue[0]:
                    set1.add(queue.popleft())
                
                set2 = set2.union(set(queue))
        
        answer.append(len(set1))
        
        print(*answer, sep="\n")            
    
    except ValueError or IndexError as e:
        print(e)
    '''
    
import sys
from collections import deque

if __name__ == "__main__":
    try:
        T = int(sys.stdin.readline())
        answer = []
        for _ in range(T):
            n = int(sys.stdin.readline())
            graph = [0] + list(map(int, sys.stdin.readline().split(" ")))
            visited = [0 for _ in range(n+1)]
            
            for idx in range(1, n+1):
                if visited[idx]:
                    continue
            
                visited[idx] = 1
                queue = deque([idx])
                
                while not visited[graph[idx]]:
                    idx = graph[idx]
                    visited[idx] = 1
                    queue.append(idx)

                node = graph[idx]
                
                if visited[node] != 1:
                    for k in queue:
                        visited[k] = 2
                    continue
                    
                while queue and node != queue[0]:
                    visited[queue.popleft()] = 2
                
                for k in queue:
                    visited[k] = 3

            rlt = 0
            for idx in visited:
                if idx == 2:
                    rlt += 1
            
            answer.append(rlt)
        
        print(*answer, sep="\n")            
    
    except ValueError or IndexError as e:
        print(e)
    