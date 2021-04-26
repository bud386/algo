import sys
input = sys.stdin.readline

num_dict = {
    'I' : 1,
    'IV' : 4,
    'V' : 5, 
    'IX' : 9,
    'X' : 10,
    'XL' : 40,
    'L' : 50,
    'XC' : 90,
    'C' : 100,
    'CD': 400,
    'D' : 500,
    'CM': 900,
    'M' : 1000
}

num = 0
for _ in range(2):
    word = input().strip()
    n = len(word)
    i = 0

    while i < n:
        if word[i] == 'I':
            if i+1 < n and (word[i+1] == 'V' or word[i+1] == 'X'):
                num += num_dict[word[i:i+2]]
                i += 2
            else:
                num += num_dict[word[i]]
                i += 1
        elif word[i] == 'X':
            if i+1 < n and (word[i+1] == 'L' or word[i+1] == 'C'):
                num += num_dict[word[i:i+2]]
                i += 2
            else:
                num += num_dict[word[i]]
                i += 1
        elif word[i] == 'C':
            if i+1 < n and ( word[i+1] == 'D' or word[i+1] == 'M'):
                num += num_dict[word[i:i+2]]
                i += 2            
            else:
                num += num_dict[word[i]]
                i += 1
        else:
            num += num_dict[word[i]]
            i += 1
        
print(num)


num = str(num)
n = len(num)
num_li = [0] * 4
idx = 4 - n

# {0, 0, 0, 0}
# 각 자리수 리스트에 넣어줌 
for i in range(n):
    num_li[idx] = int(num[i])
    idx += 1

roma_num = ''

for i in range(4):
    digit = num_li[i]
    if i == 0: 
        roma_num += digit * 'M'
    elif i == 1:
        if digit == 9:
            roma_num += 'CM'
        elif digit == 4:
            roma_num += 'CD'
        else:
            if digit >= 5:
                roma_num += 'D'
            roma_num += (digit % 5) * 'C'
    elif i == 2:
        if digit == 9:
            roma_num += 'XC'
        elif digit == 4:
            roma_num += 'XL'
        else:
            if digit >= 5:
                roma_num += 'L'
            roma_num += (digit % 5) * 'X' 
    elif i == 3:
        if digit == 9:
            roma_num += 'IX'
        elif digit == 4:
            roma_num += 'IV'
        else:
            if digit >= 5:
                roma_num += 'V'
            roma_num += (digit % 5) * 'I' 

print(roma_num)