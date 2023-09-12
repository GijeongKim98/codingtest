# 후위 표기식
'''https://www.acmicpc.net/problem/1918'''

import sys
from collections import deque

input_data = sys.stdin.readline().rstrip()

stack = deque()

result = ""

for char in input_data:
    
    priority = {"(": 0, ")": 0, "+": 1, "-": 1 ,"*": 2, "/": 2}
    
    if char.isalpha():
        result += char
    
    elif char == "(":
        stack.append(char)
    
    elif char == ")":
        pop_char = stack.pop()
        while stack and  pop_char != "(":
            result += pop_char
            pop_char = stack.pop()
    
    else:
        while stack and priority[stack[-1]] >= priority[char]:
            result += stack.pop()
        
        stack.append(char)

while stack:
    result += stack.pop()

print(result)
        
        

    