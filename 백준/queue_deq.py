# Queue
class Queue:
    def __init__(self):
        self.list_ = []
        self.tail = -1
        self.head = -1

    def get_queue(self):
        return self.list_[self.tail + 1 : self.head]

    def push(self, x):
        self.list_.append(x)
        self.head += 1

    def empty(self):
        if self.head == self.tail:
            return 1
        return 0

    def size(self):
        return self.head - self.tail

    def pop(self):
        if self.empty():
            return -1
        self.tail += 1
        return self.list_[self.tail]

    def front(self):
        if self.empty():
            return -1
        return self.list_[self.tail+1]

    def back(self):
        if self.empty():
            return -1
        return self.list_[self.head]


# 큐 2
'''https://www.acmicpc.net/problem/18258'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    queue = Queue()
    for _ in range(N):
        tup_ = tuple(sys.stdin.readline().split(' '))
        if len(tup_) == 2:
            queue.push(int(tup_[1]))
        else:
            command = tup_[0].rstrip()
            if command == 'pop':
                print(queue.pop())
            elif command == 'empty':
                print(queue.empty())
            elif command == 'size':
                print(queue.size())
            elif command == 'back':
                print(queue.back())
            elif command == 'front':
                print(queue.front())
except ValueError or IndexError:
    print('Input Error')

'''
# Queue
class QueueV2:
    def __init__(self, a = 0):
        self.list_ = list(range(a+1))
        self.tail = 0
        self.head = a
        self.length = a+1

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False


    def pop_v2(self):
        self.tail = (self.tail + 2) % self.length
        self.head = (self.head + 1) % self.length
        self.list_[self.head] = self.list_[self.tail]
        return self.list_[self.tail - 1]

# 카드 2
'''https://www.acmicpc.net/problem/2164'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    queue = QueueV2(N)
    k = 0
    while not queue.is_empty():
        k = queue.pop_v2()
    print(k)
except ValueError:
    print("Input Error")
'''
# Circular Queue
class CircularQueue:
    def __init__(self, n):
        self.list_ = [0] * (n+1)
        self.head = 0
        self.tail = 0
        self.length = n+1

    def push(self, x):
        if self.is_full():
            return
        self.head = (self.head + 1) % self.length
        self.list_[self.head] = x

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def is_full(self):
        if (self.head + 1) % self.length == self.tail:
            return True
        return False

    def pop(self):
        if self.is_empty():
            return 0
        self.tail = (self.tail + 1) % self.length
        return self.list_[self.tail]


# Router
'''https://www.acmicpc.net/problem/15828'''
'''
import sys
try:
    size = int(sys.stdin.readline())
    queue = CircularQueue(size)
    while True:
        number = int(sys.stdin.readline())
        if number < 0:
            break
        elif number == 0:
            queue.pop()
        else:
            queue.push(number)

    if queue.is_empty():
        print('empty')
    while not queue.is_empty():
        k = queue.pop()
        print(f'{k}', end=' ')
except ValueError or IndexError:
    print('Input Error')
'''
# 요세푸스 문제 0
'''https://www.acmicpc.net/problem/11866'''
'''
import sys
try:
    N, K = tuple(map(int, sys.stdin.readline().split(' ')))
    list_ = list(range(1,N+1))
    rlt = []
    bool_l = [True] * N
    count = 0
    for _ in range(N):
        i = 0
        while i < K:
            if bool_l[count]:
                i += 1
            count = (count + 1) % N

        rlt.append(list_[count-1])
        bool_l[count-1] = False

    print('<', end='')
    for i in range(N-1):
        print(f'{rlt[i]}, ',end='')
    print(f'{rlt[-1]}>')

except ValueError or IndexError:
    print('Input Error')

'''

# Circular Queue version2

class CQueueV2:
    def __init__(self, p, n):
        self.list_ = [0] + p
        self.head = n
        self.tail = 0
        self.length = n + 1

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def pop(self):
        if self.is_empty():
            return -1
        self.tail = (self.tail + 1) % self.length
        return self.list_[self.tail]

    def front(self):
        if self.is_empty():
            return -1
        return self.list_[(self.tail+1) % self.length]

    def trans_mini(self):
        self.tail = (self.tail+1) % self.length
        self.head = (self.head+1) % self.length
        self.list_[self.head] = self.list_[self.tail]

# 프린터 큐
'''https://www.acmicpc.net/problem/1966'''
'''
import sys
try:
    test = int(sys.stdin.readline())
    for _ in range(test):
        N, M = tuple(map(int, sys.stdin.readline().split(' ')))
        priority = list(map(int, sys.stdin.readline().split(' ')))

        priority_t = [k for k in enumerate(priority)]

        queue = CQueueV2(priority_t, N)

        priority.sort(reverse=True)

        count = 0 # pop count
        for pri_ in priority:
            while queue.front()[1] != pri_:
                queue.trans_mini()
            tup_ = queue.pop()
            count += 1
            if tup_[0] == M:
                break

        print(count)

except ValueError or IndexError:
    print('Input Error')
'''
# 덱
'''https://www.acmicpc.net/problem/10866'''
'''
import sys
from collections import deque

try:
    deq = deque()
    N = int(sys.stdin.readline())
    for _ in range(N):
        list_ = sys.stdin.readline().split(' ')
        if len(list_) == 2:
            if list_[0] == 'push_back':
                deq.append(int(list_[1]))
            else:
                deq.appendleft(int(list_[1]))
        else:
            command = list_[0].rstrip()
            size = len(deq)
            if command == 'pop_front':
                output = (-1 if size == 0 else deq.popleft())
            elif command == 'pop_back':
                output = (-1 if size == 0 else deq.pop())
            elif command == 'size':
                output = size
            elif command == 'empty':
                output = (1 if size == 0 else 0)
            elif command == 'front':
                output = (-1 if size == 0 else deq[0])
            elif command == 'back':
                output = (-1 if size == 0 else deq[-1])
            print(output)

except ValueError or IndexError:
    print('Input Error')
'''

# 회전하는 큐
'''https://www.acmicpc.net/problem/1021'''
'''
import sys
from collections import deque
# deque.rotate(1) : 시계 // # deque.rotate(-1) : 반시계

try:
    N, M = tuple(map(int, sys.stdin.readline().split(' ')))
    index_list = list(map(int, sys.stdin.readline().split(' ')))

    deque_ = deque(range(1,N+1))
    len_dq = N
    rlt = 0

    for idx in index_list:
        count = 0
        while deque_[0] != idx:
            deque_.rotate(1)
            count += 1

        deque_.popleft()
        rlt += (count if count < len_dq - count else len_dq - count)
        len_dq -= 1

    print(rlt)
except ValueError or IndexError:
    print('Input Error')
'''
# AC
'''https://www.acmicpc.net/problem/5430'''

# 입력
# test case
# 수행 함수 p : 1 <= p <= 1000000
# length of list : n
# list : [x_1, x_2, ..., x_n]

# 출력
# list

from collections import deque
import sys

try:
    test_case = int(sys.stdin.readline())
    for _ in range(test_case):
        func_ = sys.stdin.readline().rstrip()
        len_ = int(sys.stdin.readline())
        if len_ == 0:
            sys.stdin.readline()
            numbers = []
        else:
            numbers = list(map(int, sys.stdin.readline().lstrip('[').rstrip(']\n').split(',')))
        deque_ = deque(numbers)

        reverse_ = False
        error_ = False

        for command in func_:
            if command == 'R':
                reverse_ = (True if not reverse_ else False)
            else:
                len_ -= 1
                if len_ < 0:
                    print('error')
                    error_ = True
                    break

                if reverse_:
                    deque_.pop()
                else:
                    deque_.popleft()

        if error_:
            error_ = False
            continue

        print('[', end='')

        if len_ > 0:

            if reverse_:
                while len_ > 1:
                    len_ -= 1
                    print(deque_.pop(), end=',')
                print(deque_.pop(),end='')

            else:
                while len_ > 1:
                    len_ -= 1
                    print(deque_.popleft(), end=',')
                print(deque_.popleft(), end='')

        print(']')
except ValueError or IndexError:
    print('Input Error')









