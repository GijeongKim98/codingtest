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
'''
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
'''

# 문자열 폭발
'''https://www.acmicpc.net/problem/9935'''
'''
import sys
try:
    str_ = sys.stdin.readline().rstrip()
    bomb = sys.stdin.readline().rstrip()[::-1]

    len_b = len(bomb)
    stack_ = []
    k = 0

    for c in str_:
        stack_.append(c)
        if len(stack_) >= len_b and c == bomb[0]:
            for idx, b in enumerate(bomb):
                # print(stack_[-1 *(idx+1)])
                if stack_[-1 * (idx+1)] != b:
                    print(''.join(stack_),end='')
                    stack_ = []
                    k = 1
                    break
            if stack_:
                for i in range(len_b):
                    stack_.pop()
    if stack_ or k == 1:
        print(''.join(stack_))
    else:
        print('FRULA')

except ValueError or IndexError:
    print('Input Error')
'''

# 오큰수
'''https://www.acmicpc.net/problem/17298'''
'''
import sys
try:
    n = int(sys.stdin.readline())
    list_ = list(map(int, sys.stdin.readline().split(' ')))

    stack_ = [] # index stack
    NGE = [-1] * n

    for idx, num in enumerate(list_):
        while stack_ and list_[stack_[-1]] < num:
            NGE[stack_.pop()] = num
        stack_.append(idx)
        # print(f'NGE = {NGE} // stack_ = {stack_}')

    for i in range(n):
        print(NGE[i], end=' ')
except ValueError or IndexError:
    print('Input Error')
'''

# 오등큰수
'''https://www.acmicpc.net/problem/17299'''
'''
import sys
try:
    n = int(sys.stdin.readline())
    list_ = list(map(int, sys.stdin.readline().split(' ')))
    dict_ = dict()

    for number in list_:
        if number in dict_:
            dict_[number] += 1
        else:
            dict_[number] = 1

    # print(dict_)

    stack_ = []
    NGF = [-1] * n

    for idx, number in enumerate(list_):
        while stack_ and dict_[list_[stack_[-1]]] < dict_[number]:
            NGF[stack_.pop()] = number

        stack_.append(idx)
        # print(f'stack = {stack_} // NGF = {NGF}')
    for ngf in NGF:
        print(ngf, end=' ')

except ValueError or IndexError:
    print('Input Error')
'''

# 오아시스 재결합
'''https://www.acmicpc.net/problem/3015'''
'''
import sys
try:
    n = int(sys.stdin.readline())
    list_ = [int(sys.stdin.readline()) for _ in range(n)]

    stack_ = []
    rlt = 0

    for idx, number in enumerate(list_):
        while stack_ and list_[stack_[-1]] < number:
            rlt += idx - stack_.pop()
            print(f'rlt = {rlt} // idx = {idx}')
        stack_.append(idx)

    idx = n-1
    while stack_:
        rlt += idx - stack_.pop()

    print(rlt)
except ValueError or IndexError:
    print('Input Error')
'''


def solution(cap, n, deliveries, pickups):
    # deliveries와 pickups = stack1, stack2
    # stack1[-1] > del_ => del_ -= stack2[-1] ; stack1.pop()을 진행
    # stack2도 마찬가지
    # 이동거리 => (maximum of length of stacks + 1) * 2
    # 이동거리의 합이 결과 값

    stack1, stack2 = deliveries[:], pickups[:]
    sum_ = 0
    while stack1 or stack2:
        dis = max(len(stack1), len(stack2)) * 2
        sum_ += dis
        num_d, num_p = cap, cap

        while stack1 and stack1[-1] < num_d:
            num_d -= stack1.pop()
            print(stack1)

        while stack2 and stack2[-1] < num_p:
            num_p -= stack2.pop()

        stack1[-1] -= num_d
        stack2[-1] -= num_p
        print(f'sum = {sum_} // deliveries = {stack1} // pickups = {stack2}')
        if sum_ > 20:
            break
    answer = sum_
    return answer

print(solution(4,5,[1,0,3,1,2],[0,3,0,4,0]))