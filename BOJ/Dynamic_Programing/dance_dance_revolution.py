# Dance Dance Revolution
'''https://www.acmicpc.net/problem/2342'''

import sys

INF = 1_000_000
CASE = 5

weight = {0:{1:2,2:2,3:2,4:2},
          1:{1:1,2:3,3:4,4:3},
          2:{1:3,2:1,3:3,4:4},
          3:{1:4,2:3,3:1,4:3},
          4:{1:3,2:4,3:3,4:1}}

if __name__ == "__main__":
    try:
        commands = list(map(int, sys.stdin.readline().split(" ")))
        
        if commands[0] == 0:
            print(0)
        
        else:
            dp = [[INF for _ in range(CASE)] for _ in range(len(commands) - 1)]
            
            dp[0][0] = 2
            pre = commands[0]
            
            for new_idx, new in enumerate(commands[1:-1], start=1):
                
                if pre == new:
                    for node in range(CASE):
                        if dp[new_idx - 1][node] == INF:
                            dp[new_idx][node] = INF
                        else:    
                            dp[new_idx][node] = dp[new_idx - 1][node] + 1
                    
                    continue
                
                
                # new를 이전에 이동했던 발로 가는경우
                for another in range(CASE):
                    if another != new:
                        if pre != another:
                            dp[new_idx][another] = min(dp[new_idx - 1][another] + weight[pre][new], INF)
                        # 이전에 이동하지 않은 발로 가는 경우 계산
                        
                    dp[new_idx][pre] = min(dp[new_idx][pre], dp[new_idx - 1][another] + weight[another][new])
                
                pre = new
                        
            # print(*dp, sep="\n\n")
            
            print(min(dp[len(commands)-2]))
            
            
    except ValueError or IndexError as e:
        print(e)