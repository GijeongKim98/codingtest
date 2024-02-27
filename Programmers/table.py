SIZE = 50
EMPTY = 0

def solution(commands):
    table = [EMPTY for _ in range(SIZE*SIZE)]
    value_idx = {EMPTY:set([i for i in range(SIZE*SIZE)])}
    merge_info = {idx : [] for idx in range(SIZE*SIZE)}
    
    answer = []
    
    
    for command in commands:
        if command[1] == "P": # UPDATE r c value
            split_ = command.split(" ")
            if len(split_) == 4:
                _, r, c, value = split_
                idx = (int(r)-1)*SIZE + int(c) - 1 
                
                value_idx[table[idx]].remove(idx)
                table[idx] = value
                
                if value in value_idx:
                    value_idx[value].add(idx)
                else:
                    value_idx[value] = set([idx])
                
                for i in merge_info[idx]:
                    value_idx[table[i]].remove(i)
                    value_idx[value].add(idx)
                    table[i] = value
                        
                
            else: # UPDATE value1 value2
                _, value1, value2 = split_
                if value1 not in value_idx:
                    continue
                for idx in list(value_idx[value1]):
                    table[idx] = value2
                
                if value2 in value_idx:
                    value_idx[value2] = value_idx[value2]+value_idx[value1] 
                else:
                    value_idx[value2] = value_idx[value1]
                
                value_idx.pop(value1)
        elif command[0] == "M": # MERGE r1 c1 r2 c2
            _, r1, c1, r2, c2 = command.split(" ")
            idx1, idx2 = (int(r1)-1)*SIZE + int(c1)-1, (int(r2)-1)*SIZE + int(c2)-1
            value1, value2 = table[idx1], table[idx2]
            

            if value1 == EMPTY and value2 == EMPTY:
                for i in merge_info[idx1]:
                    merge_info[i].append(idx2)

                for i in merge_info[idx2]:
                    merge_info[i].append(idx1)

                merge_info[idx1].append(idx2)
                merge_info[idx2].append(idx1)
            
            elif value1 != EMPTY:
                for i in merge_info[idx1]:
                    merge_info[i].append(idx2)

                for i in merge_info[idx2]:
                    merge_info[i].append(idx1)
                    table[i] = value1
                    value_idx[value2].remove(i)
                    value_idx[value1].add(i)
                    
                merge_info[idx1].append(idx2)
                merge_info[idx2].append(idx1)
                value_idx[value2].remove(idx2)
                value_idx[value1].add(idx2)
                table[idx2] = value1
                if len(value_idx[value2]) == 0:
                    value_idx.pop(value2)
            
            elif value2 != EMPTY:
                for i in merge_info[idx2]:
                    merge_info[i].append(idx1)

                for i in merge_info[idx1]:
                    merge_info[i].append(idx2)
                    table[i] = value2
                    value_idx[value1].remove(i)
                    value_idx[value2].add[i]
                    
                merge_info[idx1].append(idx2)
                merge_info[idx2].append(idx1)
                value_idx[value1].remove(idx1)
                value_idx[value2].add[idx1]
                table[idx1] = value2
                if len(value_idx[value1]) == 0:
                    value_idx.pop(value1)

        elif command[0] == "U": # UNMERGE r c
            _, r, c = command.split(" ")
            idx = (int(r)-1)*SIZE+int(c)-1
            value = table[idx]
            for i in merge_info[idx]:
                value_idx[value].remove(i)
                merge_info[i] = []
                table[i] = EMPTY
            
            merge_info[idx] = []
            
        
        else: # PRINT r,c
            _, r, c = command.split(" ")
            idx = (int(r)-1)*SIZE + int(c) - 1 
            answer.append(table[idx] if table[idx] != EMPTY else "EMPTY")
            
               
    
    return answer


if __name__ == "__main__":
    c = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
    # c = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
    
    print(solution(c))