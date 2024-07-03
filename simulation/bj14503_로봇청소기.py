"""
1. 아이디어
- while 문을 돌면서 작동이 반복되는 로직을 구한다.
- 청소가 되지 않은 킨반이 없을 경우 후진한다. 
- 후진할 수 없다면 작동을 멈춘다.

- 청소되지 않은 빈칸이 있을 경우 반시계방향으로 회전해서 1칸 전진해서 청소한다.

2. 시간복잡도
- O(n*m) = 50 * 50 = 2500 < 2억 가능


3. 자료구조
- 맵구조의 n, m값
- 청소방에 대한 구조 : int[][]
- 위치정보 : 현재위치, 방향

"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
y, x, d = map(int, input().split())
room_map = [list(map(int, input().split())) for _ in range(n)]

#print(f"room_map:{room_map}")

ny = [-1,0,1,0]
nx = [0,1,0,-1]
cnt = 0
while True:
    if room_map[y][x] == 0:
        room_map[y][x] = 2
        cnt +=1

    sw = False
    for i in range(1,5):
        # 방향전환 하여 체크할 좌표 계산
        my = y + ny[d-i]
        mx = x + nx[d-i]

        if 0<= my < n and 0<= mx < m:
            if room_map[my][mx] == 0:
                d = (d - i) % 4
                y = my
                x = mx
                room_map[my][mx] =2
                cnt +=1
                sw = True
                break

    # 4방향 모두 없을 경우 뒤로 후진
    if sw == False:
        my = y - ny[d]
        mx = x - nx[d]
        if room_map[my][mx] == 1:
            break
        else:
            y = my
            x = mx 


print(cnt)