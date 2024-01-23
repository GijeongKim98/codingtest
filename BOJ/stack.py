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
'''
'''import sys

HEIGHT, CNT = 0, 1


def solve():
    stack = []
    answer = 0

    for h in arr:
        # stack에 현재 사람보다 작은 사람이 있으면 pop하고 answer에 추가
        while stack and stack[-1][HEIGHT] < h:
            answer += stack.pop()[CNT]

        # 스택이 비었으면 현재 사람을 그냥 추가
        if not stack:
            stack.append((h, 1))
            continue

        # 스택이 안 비었고, top과 지금 현재 사람의 키가 같으면
        if stack[-1][HEIGHT] == h:
            cnt = stack.pop()[CNT]
            answer += cnt

            # 현재 같은키보다 왼쪽이 있으므로 -> top과 현재 사람이 볼 수 있으므로 1추가
            if stack:
                answer += 1

            # 현재 키인 사람과 같은 사람이 cnt만큼 있으므로, 키 = h, 명수 = cnt+1를 스택에 추가
            stack.append((h, cnt + 1))

        # 스택이 안비었고, 왼쪽 사람보다 키가 작으므로 그 사람만 볼 수 있음 -> 스택에 현재 키를 넣고, answer에 1추가(왼쪽 사람만 볼 수 있으므로)
        else:
            stack.append((h, 1))
            answer += 1

    return answer


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
print(solve())
'''
# 오아시스 재결합
# 처음 틀린 코드
# 틀린이유 : 인덱스로 접근해서 pop된 사람의 오른쪽 사람들의 숫자를 계산하였다
# 6, 5, 4, 3, 2, 1 => 5-5 + 5-4 + 5-3 + 5-2 + 5-1 + 5-0 = 15
# 이런식으로 계산해서 틀렸다.
# 그래서 다른 사람의 답변을 참고했다.
# 출처
'''https://0902.tistory.com/57'''
# 이 분께서 푼 방법으로 풀어보자.
# 방법 : 현재 사람을 볼 수 있는 왼쪽 사람 수를 더하자.
# 스택에 내림차순으로 추가. => 만약 현재 스택[-1] 사람보다 더 큰 사람이 들어오려한다면
# => 스택.pop() => pop된 사람은 무조건 현재사람을 볼 수 있으므로 answer += (키가같은 사람의 수)
# 스택이 비어있다면 => 이미 pop된 사람이 존재해서 + 과정을 진행했거나, 처음 한 사람인 경우이다.
# 같은 값을 스택에 넣을 때는 pop을 해줘 같은 사람의 수를 더해 스택에 넣는다.
# 이 과정에서는 값이 같은 사람도 현재사람을 볼 수 있으므로 +1 해주고, 더불어서 넣을때 바로 왼쪽 사람도 볼수 있으므로 +1을 해준다.
# 만약 같지도 않고 비어있지않고 더 작은 사람이라면 스택에 넣고 그 사람은 왼쪽사람만 볼 수 있으므로 +1을 해준다.


# 오아시스 재결합
'''https://www.acmicpc.net/problem/3015'''

import sys
try:
    # Input
    N = int(sys.stdin.readline())
    heights = [int(sys.stdin.readline()) for _ in range(N)]

    stack_ = []
    HEIGHT, CNT = 0,1
    result = 0

    for now_height in heights:
        while stack_ and stack_[-1][HEIGHT] < now_height:
            result += stack_.pop()[CNT]

        if not stack_:
            stack_.append((now_height,1))
            # print(f'stack : {stack_}\nresult : {result} // now_height : {now_height}')
            continue

        cnt = 0
        if stack_[-1][HEIGHT] == now_height:
            cnt = stack_.pop()[CNT]
            result += cnt


        if stack_ and stack_[-1][HEIGHT] > now_height:
            result += 1

        stack_.append((now_height, cnt + 1))



        # print(f'stack : {stack_}\nresult : {result} // now_height : {now_height}')

    print(result)
except ValueError or IndexError as e:
    print(e)



