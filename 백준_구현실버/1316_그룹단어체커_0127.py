import sys

n = int(sys.stdin.readline())

words = []
for i in range(n):
    words.append(input()) 


count = 0
not_groupword = False
for word in words:
    
    if len(word) == 1:
        count += 1
    elif len(set(word)) == len(word):
        count += 1 
    else:
        for char in word:
            # print('위에 두조건 충족안할때:',char, word)
            if word.count(char) > 1:
                # print(char)
                # print(word.replace(char*word.count(char),''))
                if word.replace(char,'') != word.replace(char*word.count(char),''):
                    # print('검사 word:', word)
                    # print('알파벳: ',char)
                    # print(word.replace(char,''))
                    # print(word.replace(char*word.count(char),''))
                    # print(word, '는 그룹워드아님')
                    not_groupword = True
                    break
        if not_groupword:
            # print(word, '는 그룹워드가 아님')
            not_groupword = False
            pass
        else:
            # print(word, "는 그룹워드입니다")
            count += 1
                         

print(count)





