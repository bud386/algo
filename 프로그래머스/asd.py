def solution(new_id):    
    id = []
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for i in new_id:
        if i == '-' or i == '_' or i == '.' or '0' <= i <= '9' or 'a' <= i <= 'z':
            id.append(i)
            
    # 3단계
    cnt = 0
    correct_id = []
    for i in id:
        if i == '.':
            cnt += 1
            if cnt <= 1:
                correct_id.append(i)
        else:
            cnt = 0
            correct_id.append(i)
    
    # 4단계
    print(correct_id[-1],'ghfghd')
    while correct_id and correct_id[-1] == '.':
        correct_id.pop()
    
    while correct_id and correct_id[0] == '.':
        correct_id.pop(0)
        
    # 5단계
    if not correct_id:
        correct_id = ['a']
    
    # 6단계
    if len(correct_id) >= 16:
        correct_id = correct_id[0:15]
    while correct_id[-1] == '.':
        correct_id.pop()
        
    # 7단계
    while len(correct_id) <= 2:
        correct_id.append(correct_id[-1])
    
    answer = "".join(correct_id)
    print(answer)
    return answer

# solution("abcdefghijklmn.p")
# solution("123_.def")
solution("=.=")
# solution("z-+.^.")
# solution("...!@BaT#*..y.abcdefghijklm")