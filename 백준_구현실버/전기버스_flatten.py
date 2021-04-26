# T = int(input())

# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())  # 최대 이동 정류장수, 종점, 충전기 설치
#     M_num = list(map(int, input().split()))

#     impossible = False

#     move = 0
#     count = 0
#     now = 0
    
#     while now <= N:
#         move += 1
#         now += 1
#         if now == N:
#             if move > K:
#                 impossible = True
#             break
#         if move == K:
#             if now in M_num:
#                 count += 1
#                 move = 0
#             else:
#                 for j in range(1, K):
#                     if now - j in M_num:
#                         count += 1
#                         move = 0
#                         now = now-j
#                         break

#     if impossible:
#         print(f'#{tc} 0')
#     else:
#         print('#{} {}'.format(tc,count))






# for tc in range(1, 11):
#     dump_chance = int(input())
#     box_h = list(map(int, input().split()))

#     while dump_chance:
#         max_h = box_h[0]
#         max_idx = 0
#         min_h = box_h[0]
#         min_idx = 0
#         for i in range(len(box_h)):
#             if box_h[i] > max_h:
#                 max_h = box_h[i]
#                 max_idx = i
#             if box_h[i] < min_h:
#                 min_h = box_h[i]
#                 min_idx = i
#         box_h[max_idx] -= 1
#         box_h[min_idx] += 1
#         dump_chance -= 1

#     max_h = box_h[0]
#     max_idx = 0
#     min_h = box_h[0]
#     min_idx = 0
#     for i in range(len(box_h)):
#         if box_h[i] > max_h:
#             max_h = box_h[i]
#             max_idx = i
#         if box_h[i] < min_h:
#             min_h = box_h[i]
#             min_idx = i

#     ans = box_h[max_idx] - box_h[min_idx]
#     print(f'#{tc} {box_h[max_idx] - box_h[min_idx]}')

T = int(input())

for tc in range(1, T+1):
    # K : 이동할 수 있는거리
    # N : 마지막 종점 위치
    # M : 충전소의 개수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    # 충전소를 표시하자!
    bus_stop = [0] * (N+1)
    for i in charge:
        bus_stop[i] = 1

    bus = 0 # 버스 위치
    ans = 0
    while True:
        # 버스가 이동할 수 있는 만큼 이동을 하자
        bus += K
        if bus >= N :
            break # 종점에 도착하거나 종점지를 지나 더 나아간 경우

        for i in range(bus, bus-K, -1):
            print('AAASD', i)
            if bus_stop[i]: # == 1:
                ans += 1
                bus = i
                break

        # 충전기를 못 찾았을때
        # print('??')
        else:
            print('!!',i)
            ans = 0
            break


    print('#{} {}'.format(tc, ans))