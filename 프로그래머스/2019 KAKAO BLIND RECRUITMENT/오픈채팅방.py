def solution(record):
    answer = []
    id_name = {}
    new_record = []
    for i in record:
        
        new_record.append(i.split())
    
    for r in new_record:
        if r[0] == 'Leave':
            continue
        action, user_id, name = r        
        id_name[user_id] = name

    for r in new_record:
        action = r[0]
        user_id = r[1]        
        if action == 'Enter':
            message = id_name[user_id] + '님이 들어왔습니다.'
            answer.append(message)
        elif action == 'Leave':
            message = id_name[user_id] + '님이 나갔습니다.'
            answer.append(message)
        
    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])