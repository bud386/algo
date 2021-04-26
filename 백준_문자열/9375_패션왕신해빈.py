import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())    # 옷의 개수
    clothes_typ = []    # 옷 종류
    typ_cnt = [0] * 30  # 종류별 개수 (0 <= n <= 30)
    for _ in range(n):
        clothes, typ = map(str, (input().split()))
        if typ not in clothes_typ:  # 처음 나온 옷 종류면 옷 종류 추가
            clothes_typ.append(typ)
        typ_cnt[clothes_typ.index(typ)] += 1    # 옷 종류의 index찾고 종류별 개수의 해당 idx의 값 +1 해준다.
    
    ans = 1
    for i in range(len(clothes_typ)):
        ans *= (typ_cnt[i] + 1)          
    print(ans-1)
    
        
