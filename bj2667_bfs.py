"""
1. 아이디어
- 이중 for 문을 통해서 bfs 탐색을 하여 갯수를 구한다. 

2. 시간복잡도 O(V + E)
V : 25 * 25
E : 4 * 625
시간복잡도 : 625 + 2500 < 2억 : 가능!!


3. 알고리즘
- 데이터 맵 필요 int[][]
- 중복 처리 방지 bool[][]
- 집수 list

"""

import sys
input = sys.stdin.readline

n = int(input())

data = [list(map(int,input().strip())) for _ in range(n)]

chk = [[False] * n for _ in range(n)]
rs_list = []


hy = [0,1,0,-1]
hx = [1,0,-1,0]

# bfs함수
def bfs(y, x):
    p = [(y,x)]
    rs = 1
    while p:
        ny, nx = p.pop()
        for h in range(4):
            my = ny+hy[h]
            mx = nx+hx[h]
            if 0<=my<n and 0<=mx<n:
                if data[my][mx]==1 and chk[my][mx]==False:
                    chk[my][mx] = True
                    rs += 1
                    p.append((my,mx))
    return rs




# 처리 함수
for y in range(n):
    for x in range(n):
        if data[y][x]==1 and chk[y][x]==False:
            chk[y][x] = True

            rs_list.append(bfs(y,x))


print(len(rs_list))
rs_list = sorted(rs_list)
for value in rs_list:
    print(value)

