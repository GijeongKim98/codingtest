# programmers : 가장 많이 받은 선물

def solution(friends, gifts):
    answer = 0
    
    len_ = len(friends)
    name2id = {name : idx for idx, name in enumerate(friends)}
    
    # 선물 기록 저장 : {이름 : 받은 선물 -1 준 선물 +1}
    # list에 저장
    gift_info = [[0 for _ in range(len_)] for _ in range(len_)]
    
    # 선물 지수
    gift_number = [0 for _ in range(len_)]
    
    for str_ in gifts:
        a, b = str_.split(" ")
        a, b = name2id[a], name2id[b]
        
        gift_info[a][b] += 1
        gift_info[b][a] -= 1
        
        gift_number[a] += 1
        gift_number[b] -= 1
        
    rst = [0 for _ in range(len_)]
    
    for a in range(len_):
        for b in range(a+1, len_):
            if gift_info[a][b] < 0: # a가 선물을 적게준 경우
                rst[b] += 1
                
            elif gift_info[a][b] > 0: # a가 선물을 많이 준 경우
                rst[a] += 1
                
            else: # 같은 경우
                if gift_number[a] > gift_number[b]:
                    rst[a] += 1
                
                elif gift_number[a] < gift_number[b]:
                    rst[b] += 1
    
    answer = max(rst)
    
    return answer

if __name__ == "__main__":
    friends = ["muzi", "ryan", "frodo", "neo"]
    gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
    
    friends = ["joy", "brad", "alessandro", "conan", "david"]
    gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
    
    friends = ["a", "b", "c"]
    gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
    ans = solution(friends, gifts)
    
    print(ans)