# 최대 힙
# Max heap
class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def is_empty(self):
        if len(self.heap) == 1:
            return True
        return False

    def insert(self,x):
        self.heap.append(x)
        key = len(self.heap) - 1
        p = key // 2
        while p > 0 and self.heap[p] < x:
            self.heap[key], self.heap[p] = self.heap[p], self.heap[key]
            key = p
            p = p // 2

    def delete(self):
        if self.is_empty():
            return 0
        self.heap[-1], self.heap[1] = self.heap[1], self.heap[-1]
        rlt = self.heap.pop()
        len_ = len(self.heap) - 1
        p = 1
        if len_ >= p*2 + 1:
            c =(p*2 if self.heap[p*2] > self.heap[p*2+1] else p*2+1)
        elif len_ == p*2:
            c = p * 2
        else:
            return rlt
        while c <= len_ and self.heap[c] > self.heap[p]:
            self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
            p = c
            if len_ >= p * 2 + 1:
                c = (p * 2 if self.heap[p * 2] > self.heap[p * 2 + 1] else p * 2 + 1)
            elif len_ == p * 2:
                c = p * 2
            else:
                break
        return rlt

'''https://www.acmicpc.net/problem/11279'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    max_h = MaxHeap()

    for _ in range(N):
        comm = int(sys.stdin.readline())
        if comm > 0:
            max_h.insert(comm)
        else:
            print(max_h.delete())
        #print(max_h.heap)
except ValueError or IndexError:
    print('Input Error')

# 최소 힙
# Min heap
class MinHeap:
    def __init__(self):
        self.heap = [None]

    def is_empty(self):
        if len(self.heap) == 1:
            return True
        return False

    def insert(self,x):
        self.heap.append(x)
        key = len(self.heap) - 1
        p = key // 2
        while p > 0 and self.heap[p] > x:
            self.heap[key], self.heap[p] = self.heap[p], self.heap[key]
            key = p
            p = p // 2

    def delete(self):
        if self.is_empty():
            return 0
        self.heap[-1], self.heap[1] = self.heap[1], self.heap[-1]
        rlt = self.heap.pop()
        len_ = len(self.heap) - 1
        p = 1
        if len_ >= p*2 + 1:
            c =(p*2 if self.heap[p*2] < self.heap[p*2+1] else p*2+1)
        elif len_ == p*2:
            c = p * 2
        else:
            return rlt
        while c <= len_ and self.heap[c] < self.heap[p]:
            self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
            p = c
            if len_ >= p * 2 + 1:
                c = (p * 2 if self.heap[p * 2] < self.heap[p * 2 + 1] else p * 2 + 1)
            elif len_ == p * 2:
                c = p * 2
            else:
                break
        return rlt
'''
'''https://www.acmicpc.net/problem/1927'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    min_h = MinHeap()

    for _ in range(N):
        comm = int(sys.stdin.readline())
        if comm > 0:
            min_h.insert(comm)
        else:
            print(min_h.delete())
        #print(max_h.heap)
except ValueError or IndexError:
    print('Input Error')
'''
'''
# 절댓값 힙
class AbsoluteHeap:
    def __init__(self):
        self.heap = [-1]

    def is_empty(self):
        if len(self.heap) == 1:
            return True
        return False

    def insert(self, x):
        abs_ = abs(x)
        self.heap.append(x)
        c = len(self.heap) - 1
        p = c//2
        while p > 0 and abs(self.heap[p]) >= abs_:
            if abs(self.heap[p]) == abs_ and self.heap[p] < x:
                break
            self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
            c = p
            p = c // 2

    def delete(self):
        if self.is_empty():
            return 0
        self.heap[-1], self.heap[1] = self.heap[1], self.heap[-1]
        rlt = self.heap.pop()
        len_ = len(self.heap) - 1
        p = 1
        c = 1
        while len_ > p*2:
            c = p*2
            if c+1 <= len_:
                if abs(self.heap[c]) > abs(self.heap[c + 1]) or (abs(self.heap[c]) == abs(self.heap[c+1]) and self.heap[c+1]<self.heap[c]):
                    c = c + 1
            if abs(self.heap[c]) > abs(self.heap[p]) or (abs(self.heap[c]) == abs(self.heap[p]) and self.heap[c]>self.heap[p]):
                break
            self.heap[c],self.heap[p] = self.heap[p],self.heap[c]
            p = c
        return rlt

import sys
try:
    n = int(sys.stdin.readline())
    abs_heap = AbsoluteHeap()
    for _ in range(n):
        comm = int(sys.stdin.readline())
        if comm == 0:
            print(abs_heap.delete())
        else:
            abs_heap.insert(comm)
        #print(abs_heap.heap)
except ValueError or IndexError:
    print('Input Error')


'''
# 가운데를 말해요
'''https://www.acmicpc.net/problem/1655'''

class TwoHeap:
    def __init__(self):
        self.min_h = [None]
        self.max_h = [None]

    def min_is_empty(self):
        if len(self.min_h) == 1:
            return True
        return False

    def max_is_empty(self):
        if len(self.max_h) == 1:
            return True
        return False

    def max_append(self, x):
        self.max_h.append(x)
        c = len(self.max_h) - 1
        p = c // 2
        while p > 0 and self.max_h[p] < x:
            self.max_h[c],self.max_h[p] = self.max_h[p], self.max_h[c]
            c = p
            p = c // 2


    def max_pop(self):
        self.max_h[1],self.max_h[-1] = self.max_h[-1], self.max_h[1]
        rlt = self.max_h.pop()
        p = 1
        len_ = len(self.max_h) - 1
        while p*2 <= len_:
            c = p*2
            if c+1 <= len_:
                c = (c if self.max_h[c] > self.max_h[c+1] else c+1)
            if self.max_h[c] < self.max_h[p]:
                break
            self.max_h[p], self.max_h[c] = self.max_h[c], self.max_h[p]
            p = c
        return rlt


    def min_append(self, x):
        self.min_h.append(x)
        c = len(self.min_h) - 1
        p = c // 2
        while p > 0 and self.min_h[p] > x:
            self.min_h[c], self.min_h[p] = self.min_h[p], self.min_h[c]
            c = p
            p = c // 2

    def min_pop(self):
        self.min_h[1], self.min_h[-1] = self.min_h[-1], self.min_h[1]
        rlt = self.min_h.pop()
        p = 1
        len_ = len(self.min_h) - 1
        while p * 2 <= len_:
            c = p * 2
            if c + 1 <= len_:
                c = (c if self.min_h[c] < self.min_h[c + 1] else c + 1)
            if self.min_h[c] > self.min_h[p]:
                break
            self.min_h[p], self.min_h[c] = self.min_h[c], self.min_h[p]
            p = c
        return rlt

    def insert_print(self,x):
        if self.max_is_empty():
            self.max_append(x)

        elif self.min_is_empty():
            self.max_append(x)
            self.min_append(self.max_pop())

        else:
            if self.min_h[1] < x:
                self.min_append(x)
                if len(self.min_h) > len(self.max_h):
                    self.max_append(self.min_pop())
            else:
                self.max_append(x)
                if len(self.min_h) + 2 == len(self.max_h):
                    self.min_append(self.max_pop())

        return self.max_h[1]

import sys
try:
    n = int(sys.stdin.readline())
    t_heap = TwoHeap()
    for _ in range(n):
        number = int(sys.stdin.readline())
        print(t_heap.insert_print(number))
        # print(f'max_heap = {t_heap.max_h}')
        # print(f'min_heap = {t_heap.min_h}')
except ValueError or IndexError:
    print('Input Error')