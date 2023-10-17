# 계단 수
'''https://www.acmicpc.net/problem/1562'''

# 필요 함수 정리

# Visited All Number 
VAN = (1 << 10) - 1

CONSTANT = 1000_000_000

def dfs(step, visited, last_number):
    if step == N:
        if visited == VAN:
            # print(f"step : {step}, visited = {bin(visited)}, last_number = {last_number}, count = {1}")
            # for n in stack:
            #     print(n, end="")
            # print()
            return 1
        else:
            return 0
        
    if (step, visited, last_number) in dp.keys():
        return dp[(step, visited, last_number)]
    
    count = 0
    if last_number == 9:
        new_number = 8
        count += dfs(step+1, visited | (1<<new_number), new_number)
        count = count % CONSTANT
    
    elif last_number == 0:
        new_number = 1
        count += dfs(step+1, visited | (1<<new_number), new_number)
        count = count % CONSTANT
    
    else:
        for new_number in [last_number-1, last_number+1]:
            count += dfs(step+1, visited | (1<<new_number), new_number)
            count = count % CONSTANT
    
    dp[(step, visited, last_number)] = count
    
    return count
            
if __name__ == "__main__":
    try:
        N = int(input())
        stack = []
        dp = dict()
        answer  = 0 
        for i in range(1, 10):
            stack = [i]        
            answer += dfs(1,(1<<i),i)
            answer = answer % CONSTANT
        
        # for (s,v,l), c in dp.items():
        #     if c:
        #         print(f"step : {s}, visited = {bin(v)}, last_number = {l}, count = {c}")
        
        print(answer)
        
    except ValueError or IndexError as e:
        print(e)