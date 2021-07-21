import copy
candidate_key = []
answer = 0

def comb(n, r, k, key, relation):
    global answer

    if len(key) == r: # 조합 (r개 뽑았을때)
        # 유일성 검사
        pick = []
        for info in relation: # 각 학생의 정보들
            tmp = [info[i] for i in key] # 학생의 i 번쨰 속성들    
            if tmp in pick: # 같은 속성값을 지닌게 pick에 있으면 break (유일성 검사 탈락)              
                break
            else:
                pick.append(tmp)
        
        # 최소성 검사(부분집합인지)
        else:
            flag = False                        
            for c_key in candidate_key: 
                cnt = 0
                for attr in c_key:
                    if attr in key:
                        cnt += 1
                # 후보키가 현재 검사중인 key(속성조합)의 부분집합이면 최소성 탈락(flag =true)                   
                if cnt == len(c_key):
                    flag = True
                    break                
            if flag == False:
                candidate_key.append(copy.deepcopy(key))                
                answer += 1            
                                
        return

    for i in range(k, n):
        key.append(i)
        comb(n, r, i + 1, key, relation)
        key.pop()    
    
def solution(relation):
    global answer
    n = len(relation[0])    
    
    for i in range(n):        
        comb(n, i+1, 0, [], relation)    
    
    print(answer, '?')            
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)


# arr =[]
# for i in range(10):
#     key = i
#     arr.append(pick)

# print(arr)
