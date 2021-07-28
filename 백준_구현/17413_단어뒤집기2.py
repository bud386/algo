import sys

data_input = sys.stdin.readline().strip()

data_replace = data_input.replace('>', '>/').replace('<', '/<') # /<   space   >/space space space/<    spa   c e>/
data_split = data_replace.split('/') # ['', '<   space   >', 'space space space', '<    spa   c e>', ''] /<..>/ /<..>/
data = [i for i in data_split if i] # ['<   space   >', 'space space space', '<    spa   c e>'] # 빈 문자열 삭제

for i in range(len(data)):
    if '<' not in data[i]:
        data[i] = data[i].split() # 태그가 아닌 문자열에 대해서 공백을 기준으로 리스트로 나눔
        for j in range(len(data[i])):
            data[i][j] = data[i][j][::-1]

# ['<   space   >', ['space', 'space', 'space'], '<    spa   c e>']
for word in data:
    if type(word) == list:
        print(*word, end='')
    else:
        print(word, end='')


# 단어문제는 한번만 순회하는게 좋음