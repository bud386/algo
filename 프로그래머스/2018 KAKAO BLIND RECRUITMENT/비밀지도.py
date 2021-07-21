def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = arr1[i] | arr2[i]
        arr = str(bin(num)[2:])
        while len(arr) != n:
            arr = '0'+ arr
        arr = arr.replace('1', '#')
        arr = arr.replace('0', ' ')
        answer.append(arr)
    return answer