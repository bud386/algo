import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    flag = False
    n = int(input())
    numbers = [input().strip() for i in range(n)]    
    numbers.sort()
    print(numbers)
    for i in range(n-1):
        num1 = numbers[i]
        len1 = len(num1)
        for j in range(i+1, n):
            num2 = numbers[j]
            # print(num1, num2)
            if len(num2) > len1:
                if num2[:len1] == num1:
                    print('NO')
                    flag = True
                    break
        if flag:
            break
    if flag == False:
        print('YES')

for i in range(7, 5):
    print('ds')