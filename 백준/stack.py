# stack
class Stack:
    def __init__(self):
        self.list_ = []

    def empty(self):
        if self.list_:
            return 0
        return 1

    def push(self, x):
        self.list_.append(x)
        # print('+')

    def pop(self):
        # print('-')
        if self.empty() == 0:
            rlt = self.list_[-1]
            self.list_ = self.list_[:-1]
            return rlt
        return -1

    def size(self):
        return len(self.list_)

    def top(self):
        if self.empty() == 0:
            return self.list_[-1]
        return -1
    def init(self):
        self.list_ = []

# 스택
'''https://www.acmicpc.net/problem/10828'''
'''
import sys

try:
    stack = Stack()
    N = int(sys.stdin.readline())
    for _ in range(N):
        list_ = sys.stdin.readline().split(' ')
        # print(list_)
        if len(list_) == 2:
            stack.push(int(list_[1]))
        else:
            command = list_[0].rstrip()
            if command == 'pop':
                print(stack.pop())
            elif command == 'top':
                print(stack.top())
            elif command == 'empty':
                print(stack.empty())
            elif command == 'size':
                print(stack.size())
except ValueError or IndexError:
    print('Input Error')
'''

# 제로
'''https://www.acmicpc.net/problem/10773'''
'''
import sys
try:
    list_ = []
    K = int(sys.stdin.readline())
    for _ in range(K):
        number = int(sys.stdin.readline())
        if number == 0 and list_:
            list_.pop()
        else:
            list_.append(number)
    print(sum(list_))
except ValueError:
    print('Input Error')
'''

# 괄호
'''https://www.acmicpc.net/problem/9012'''
'''
import sys
try:
    T = int(sys.stdin.readline())
    for _ in range(T):
        str_ = sys.stdin.readline().rstrip()
        rlt = 0
        for char in str_:
            if char == '(':
                rlt += 1
            elif char == ')':
                rlt -= 1
                if rlt < 0 :
                    break
        if rlt == 0:
            print('YES')
        else:
            print('NO')
except ValueError:
    print('Input Error')
'''
# 균형잡힌 세상
'''https://www.acmicpc.net/problem/4949'''
'''
import sys
try:
    rlt = []
    stack = Stack()
    while True:
        str_ = sys.stdin.readline().rstrip()
        if str_ == '.':
            break
        c = 0
        for char in str_:
            if char == '(':
                stack.push('(')
            elif char == '[':
                stack.push('[')
            elif char == ')':
                if stack.pop() != '(':
                    c = 1
                    break
            elif char == ']':
                if stack.pop() != '[':
                    c = 1
                    break
        if stack.empty() == 0 or c == 1:
            rlt.append(False)
        else:
            rlt.append(True)
        stack.init()

    for b in rlt:
        if b:
            print('yes')
        else:
            print('no')

except ValueError:
    print('Input Error')
'''
# 스택 수열
'''https://www.acmicpc.net/problem/1874'''
'''
import sys
try:
    n = int(sys.stdin.readline())
    answer = [int(sys.stdin.readline()) for _ in range(n)]
    stack = Stack()
    rlt = []

    j = 0
    for i in range(1,n+1):
        stack.push(i)
        rlt.append('+')

        while j < n and answer[j] == stack.top() :
            stack.pop()
            rlt.append('-')
            j += 1

    if stack.empty() == 0:
        print('N0')
    else:
        for char in rlt:
            print(char)
except ValueError:
    print('Input Error')
'''

# 스택 수열
'''https://www.acmicpc.net/problem/1874'''
'''
import sys
try:
    n = int(sys.stdin.readline())
    answer = [int(sys.stdin.readline()) for _ in range(n)]
    stack = []
    rlt = []

    j = 0
    for i in range(1,n+1):
        stack.append(i)
        rlt.append('+')

        while j < n and answer[j] == stack[-1] :
            stack.pop()
            rlt.append('-')
            j += 1
            if not stack:
                break

    if stack:
        print('N0')
    else:
        for char in rlt:
            print(char)

except ValueError:
    print('Input Error')

'''
# 히스토그램
'''https://www.acmicpc.net/problem/1725'''

import sys
try:
    n = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(n)]
    stack_ = []
    i = 0
    max_area = 0
    while i < n:
        while stack_ and numbers[stack_[-1]] > numbers[i]:
            height = numbers[stack_.pop()]
            width = (i if not stack_ else i - stack_[-1] - 1)
            max_area = max(max_area, height*width)
        stack_.append(i)
        i+=1
    while stack_:
        height = numbers[stack_.pop()]
        width = (i if not stack_ else i - stack_[-1] - 1)
        max_area = max(max_area, height*width)
    print(max_area)
except ValueError or IndexError:
    print('Input Error')
