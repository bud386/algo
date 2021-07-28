import sys

n = int(sys.stdin.readline()) # 스위치 개수
switch = list(map(int, sys.stdin.readline().split())) # 스위치 상태
student_num = int(sys.stdin.readline()) # 학생 수
gender_switch = [list(map(int, sys.stdin.readline().split())) for _ in range(student_num)] # [성별, 학생이 입력받은 스위치 번호]

for i in range(student_num):
    num = gender_switch[i][1] # 학생이 입력받은 스위치 번호
    if gender_switch[i][0] == 1: # 성별
        for j in range(n): 
            if (j+1) % num == 0: 
                if switch[j] == 1:
                    switch[j] = 0
                else: 
                    switch[j] = 1

    elif gender_switch[i][0] == 2:
        num -= 1 # 입력받은 스위치 번호를 인덱스로
        if switch[num]:
            switch[num] = 0
        else:
            switch[num] = 1
        k = 1
        l = num - k # 왼쪽 인덱스
        r = num + k # 오른쪽 인덱스
        while 0 <= l and r < n and switch[l] == switch[r]:
            if switch[l] == 1:
                switch[l] = 0
                switch[r] = 0
            else:
                switch[l] = 1
                switch[r] = 1
            k += 1
            l = num - k
            r = num + k

cnt = 0
for i in switch:
    print(i, end = ' ')
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0





