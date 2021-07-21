def solution(info, query):
    answer = []
    new_info = []
    for i in info:
        data = i.split()
        data.append('-')
        new_info.append(data)    
        
    for q in query: # 모든 조건엗 대해
        cnt = 0
        conditions = q.split()
        for data in new_info: # 모든 지원자 data에 대해
            print(data, conditions)            
            if conditions[0] not in data:
                continue
            if conditions[2] not in data:
                continue
            if conditions[4] not in data:
                continue
            if conditions[6] not in data:
                continue
            if int(conditions[7]) > int(data[4]):
                continue
            cnt += 1                
        answer.append(cnt)
                                    
    print(answer)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)




# 학일님풀이
information = {}

def solution(info, query):
    
    for i in info:
        tmp = i.split()
        makeIt(tmp, "", 0)
        
    for key, value in information.items():
        information[key] = sorted(value)
        
    answer = []
    for q in query:
        tmp = q.split()
        word = ""
        
        for s in tmp[:len(tmp)-1]:
            if s!="and":
                word += s
                
        if word not in information:
            answer.append(0)
            continue
            
        score = information[word]
        std = int(tmp[-1])
        l, r = 0, len(score)-1
        
        while l<=r:
            mid = (l+r)//2
            if std <= score[mid]:
                r = mid-1
            else:
                l = mid+1
                
        answer.append(len(score)-l)
        
    return answer

def makeIt(arr, word, i):
    
    if i==len(arr)-1:
        if word not in information:
            information[word] = []
        information[word].append(int(arr[i]))
        return 
    
    makeIt(arr, word+arr[i], i+1)
    makeIt(arr, word+"-", i+1)