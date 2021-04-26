import sys
input = sys.stdin.readline

t = int(input())

def palindrom(word):
    # 단어의 시작과 끝
    start = 0
    end = len(word) - 1
  
    delete = False # 문자가 한번 지워진지 확인
    L_del = True    # 왼쪽 문자 지우고 회문이 성립하는지 확인

    while start < end:
        # 양 끝 확인해서 문자가 맞지 않을때
        if word[start] != word[end]:
            
            # 문자가 한번 지워진적이 있다면
            if delete == True:
                return 2
            
            # 왼쪽, 오른쪽 지웠봤는데 둘다 회문이 성립안할때
            if word[start + 1] != word[end] and word[start] != word[end - 1]:
                return 2

            # 왼쪽에서 문자 하나를 빼는 경우
            # a b c d d c d b a ===> 이런 반례가 있어서 회문 검사 필요. (word[start + 1] == word[end] and word[start] == word[end - 1])
            s, e = start, end
            if word[start + 1] == word[end]:
                delete = True
                s += 2
                e -= 1
                while s < e:
                    if word[s] != word[e]:
                        L_del = False # 왼쪽 문자 빼고 검사해봤는데 회문이 아니다.
                        break
                    s += 1
                    e -= 1
                if L_del:
                    return 1
            
            # 왼쪽에서 문자 하나를 빼고 회문검사했는데 회문이 아닐 때,
            # 오른쪽에서 문자 하나를 빼는 경우
            if word[start] == word[end - 1]:
                delete = True
                start += 1
                end -= 2
        
        else:
            start += 1
            end -= 1

    # 유사회문
    if delete:
        return 1
    # 그냥 회문
    else:
        return 0 

for _ in range(t):
    word = input().strip()
    print(palindrom(word))