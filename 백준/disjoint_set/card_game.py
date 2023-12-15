# 카드 게임
'''https://www.acmicpc.net/problem/16566'''

import sys


def find(c):
    if c == under_bounded[c]:
        return c
    
    under_bounded[c] = find(under_bounded[c])
    
    return under_bounded[c]

def search_card(c):
    c = find(c)
    
    under_bounded[c] = find(c+1)
    
    return c
    

if __name__ == "__main__":
    try:
        N, M, K = map(int, sys.stdin.readline().split(" "))
        m_cards = list(map(int, sys.stdin.readline().split(" ")))
        c_cards = list(map(int, sys.stdin.readline().split(" ")))
        
        m_cards.sort()
        
        m_idx = 0
        
        under_bounded = [N for num in range(N+1)]
        
        for num in range(1, N+1):
            if m_idx < len(m_cards)-1 and num > m_cards[m_idx]:
                m_idx += 1
            
            if num <= m_cards[m_idx]:
                under_bounded[num] = m_cards[m_idx]

            else:
                under_bounded[num] = N
        
        answer = []
        
        for card in c_cards:
            s = search_card(card+1)
            answer.append(s)
        
        print(*answer, sep="\n")
    
    except ValueError or IndexError as e:
        print(e)