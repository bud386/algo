def mergeSort(a):
    if len(a) > 1: # 배열의 길이가 1보다 클 경우 재귀함수 호출 반복
        mid = len(a)//2 # 2로 나눈 몫 (중간 값) 취함
        left, right = a[:mid], a[mid:] # left 중간 값을 기준으로 왼쪽, right 중간 값을 기준으로 오른쪽
        
        mergeSort(left) # 왼쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        mergeSort(right) # 오른쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        
        li, ri, i = 0, 0, 0 # 정렬을 위한 변수 선언 (왼쪽, 오른쪽, 기준)
        while li < len(left) and ri < len(right): # 서브 리스트의 정렬이 끝날 때까지 반복
            if left[li] < right[ri]: # 오른쪽 리스트의 값이 클 경우라면
                a[i] = left[li] # 왼쪽 리스트의 해당 인덱스의 값을 할당
                li += 1 # 왼쪽 리스트의 인덱스 하나 증가
            else: # 왼쪽 리스트의 값이 클 경우라면
                a[i] = right[ri] # 오른쪽 리스트의 해당 인덱스의 값을 할당
                ri += 1 # 오른쪽 리스트의 인덱스 하나 증가
            i += 1 # 기준 인덱스 증가
        
        if li == len(left):
            a[i:] = right[ri:]
        else:
            a[i:] = left[li:]
        return a
      # 왼쪽 리스트의 인덱스의 값이 서브 리스트의 값과 같지 않을 경우라면(정렬 끝),
      # 왼쪽 서브 리스트의 값을 리스트에 덮어쓰기, 그렇지 않은 경우라면 오른쪽 서브 리스트의 값 할당                                   
print(mergeSort([5,4,3,2,1]))


def merge(left, right):
    ans = []
    li, ri = 0, 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            ans.append(left[li])
            li += 1
        else:
            ans.append(right[ri])
            ri += 1

    if li == len(left):
        ans += right[ri:]
    else:
        ans += left[li:]
    return ans

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left, right = a[:mid], a[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


print(merge_sort([5,4,3,2,1,1]))
a = hash('a')
print(a)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    small, equal, big = [], [], []
    for num in arr:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            big.append(num)
        else:
            equal.append(num)
    return quick_sort(small) + equal + quick_sort(big)



# hash_table = list([0 for i in range(8)])
# print(type(hash_table))
hash_table = [0 for i in range(8)]
# print(type(hash_table2))
def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value
    
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
print(read_data('Dave'))

has