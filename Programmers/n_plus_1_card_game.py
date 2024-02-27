# n + 1 카드게임
# 문제 요약 설명
# 입력
#  - coin : 매 라운드 마다 제공되는 2장의 카드중 카드를 선택하면 -1
#  - cards : card들이 들어 있는 리스트 / 크기 n => 1, ..., n의 숫자가 써진 카드
#       - 게임을 시작하기 전 n // 3 장의 카드를 지니고 시작
#       - 매 라운드 마다 2장의 카드를 제공
#       - 매 라운드 마다 합이 n+1이 되는 카드를 반납해야함

# 출력
#  - 도달 가능한 최대 라운드를 출력


# 문제 해결 방법
# 완전 탐색을 기반으로 코드를 구현할 것이다.
# 처음 상태
# h : n+1을 만들 수 있는 카드 조합의 수 
# now_set : 현재 지니고 있는 카드, 처음 받는 카드(n//3)장의 카드중 n+1을 만들 수 있는 카드를 제외

# 매 라운드 마다 해줘야할 작업
## - h 갱신 : 해당 라운드에 뽑을 수 있는 2장의 카드중 
#             n+1을 바로 만들 수 있는 카드가 있다면 해당 카드는 코인의 개수에 따라 무조건 선택해야한다.

# case 1. coin >= 2: 
#   - h == 0
#       - 해당 라운드에서 제공되는 카드가 n+1을 만들 수 없는 경우 => 종료
#       - n+1을 만들 수 있는 경우
#           - 2개의 h를 만들 수 있는 경우 : (coin-2, h + 1)을 한 채로 다음 라운드
#           - 1개의 h를 만들 수 있는 경우 :
#               - 제공되는 카드의 합이 n+1인 경우 (coin-2, h)를 한 채로 다음 라운드 
#               - 첫번째 혹은 두번째 카드가 현재 지닌 카드(now_set)와 조합이 n+1이 되는 경우
#                 [] 조합을 만든다. // 두 가지의 경우가 존재 나머지 한개의 카드를 선택 여부에 따라
#                   - 나머지 카드 선택 (coin - 2, h)
#                   - 나머지 카드 선택 x (coin-1, h)
#   - h > 0
#       - 해당 라운드에서 제공되는 카드가 n+1을 만들 수 없는 경우
#           - 카드 선택 x (coin, h-1)
#           - 1장의 카드 선택 (coin-1, h-1)
#           - 2장의 카드 선택 (coin-2, h-1)
#       - n+1을 만들 수 있는 경우 
#           - 2개의 조합 생성 가능 (coin-2, h+1)로 진행
#           - 1개의 조합 생성 가능 :
#               - 제공되는 카드의 합이 n+1인 경우 (coin-2, h)를 한 채로 다음 라운드 
#               - 첫번째 혹은 두번째 카드가 현재 지닌 카드(now_set)와 조합이 n+1이 되는 경우
#                 [] 조합을 만든다. // 두 가지의 경우가 존재 나머지 한개의 카드를 선택 여부에 따라
#                   - 나머지 카드 선택 (coin - 2, h)
#                   - 나머지 카드 선택 x (coin-1, h)

# case 2. coin == 1:
#   - 조합을 만들 수 있는 경우 >= 1 => 종료 : 현재 라운드 + h
#   - 조합을 만들 수 있는 경우 == 0
#          # h == 0 : 종료 현재 라운드
#          # h >=1 이면 생존 (coin, h-1)  

# case 3. coin == 0:
#  - 종료 현재라운드 + h


# 매 라운드 마다 h를 갱신 및 h -= 1을 수행

# 따라서 반드시 가져와야하는 카드가 존재할 것이다.

# def solution(coin, cards):
#     def dfs(step, coin, heart):
#         if coin == 0:
#             return step+heart
        
#         card1, card2 = cards[step*2+n//3], cards[step*2+n//3+1]
#         c1, c2, c3 = (n+1-card1) in now_set, (n+1-card2) in now_set, n+1 == card1+card2
        
#         if coin == 1:
#             if c1:
#                 return step+heart+1
#             elif c2:
#                 return step+heart+1
#             else:
#                 if heart == 0:
#                     return step
#                 else:
#                     return dfs(step+1,coin,heart-1)
        
#         else:
#             if not c1 and not c2 and not c3:
#                 if heart == 0:
#                     return step
                
#                 else:
#                     # card 선택 x
#                     max_round = dfs(step+1,coin,heart-1)
                    
#                     # card1 선택
#                     now_set.add(card1)
#                     max_round = max(max_round, dfs(step+1, coin-1, heart-1))
                    
#                     # 2장의 카드 선택
#                     now_set.add(card2)
#                     max_round = max(max_round, dfs(step+1, coin-1, heart-1))
                    
#                     # card2 선택
#                     now_set.remove(card1)
#                     max_round = max(max_round, dfs(step+1,coin-1, heart-1))
                    
#                     # 종료
#                     now_set.remove(card2)
#                     return max_round
            
#             elif c1 and c2:
#                 return dfs(step+1,coin-2,heart+1)
            
#             elif c3:
#                 if heart == 0:
#                     return dfs(step+1, coin-2, heart)
#                 else:
#                     max_round = dfs(step+1,coin,heart-1)
                    
#                     now_set.add(card1)
#                     now_set.add(card2)
#                     max_round = max(max_round, dfs(step+1,coin-2,heart))
#                     now_set.remove(card1)
#                     now_set.remove(card2)
#                     return max_round        
            
#             elif c1:
#                 max_round = dfs(step+1,coin-1,heart)
#                 now_set.add(card2)
#                 max_round = max(max_round, dfs(step+1,coin-2,heart))
#                 now_set.remove(card2)
#                 return max_round
                
            
#             elif c2:
#                 max_round = dfs(step+1,coin-1,heart)
#                 now_set.add(card1)
#                 max_round = max(max_round, dfs(step+1,coin-2,heart))
#                 now_set.remove(card1)
#                 return max_round
               
    
    
#     n = len(cards)
#     now_set = set(cards[:n//3])
#     heart = 0
    
#     for card in cards[:n//3]:
#         if n+1-card in now_set:
#             now_set.remove(card)
#             now_set.remove(n+1-card)
#             heart += 1
    
#     answer = dfs(0, coin, heart)
    
#     return answer + 1

def solution(coin, cards):
    def is_n_plus_1(s1, s2):
        for card in list(s1):
            if n+1-card in s2:
                s1.remove(card)
                s2.remove(n+1-card)
                return True
        return False
    
    round = 0
    n = len(cards)
    initial_cards = set(cards[:n//3])
    get_cards = set()
    
    while round < n//3:
        card1, card2 = cards[2*round+n//3], cards[2*round+n//3+1]
        get_cards.add(card1)
        get_cards.add(card2)
        round += 1
        
        if is_n_plus_1(initial_cards,initial_cards):
            continue
        
        elif coin >= 1 and is_n_plus_1(initial_cards, get_cards):
            coin -= 1
            continue
        
        elif coin >= 2 and is_n_plus_1(get_cards, get_cards):
            coin -= 2
            continue
        
        else:
            break
        
    answer = round
    return answer

if __name__ == "__main__":
    c, cards = 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    ans = solution(c, cards)
    print(ans)