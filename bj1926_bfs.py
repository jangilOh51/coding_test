
"""
1. 아이디어 
- BFS (Breadth-first search) 너비우선탐색
- 2중 for => 값 1 && 방문 X => BFS
- BFS 돌면서 그림 개수 +1 , 최대값을 갱신


2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < 2억 : 가능!!

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문여부 : bool[][]
- Queue (BFS)
"""


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data_map = [list(map(int, input().split())) for _ in range(n)]
visit_chk = [[False]* m for _ in range(n)]

img_cnt = 0
maxv = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if data_map[ny][nx] ==1 and visit_chk[ny][nx] == False:
                    rs +=1
                    visit_chk[ny][nx] = True

                    q.append((ny, nx))

    return rs

for y in range(n):
    for x in range(m):
        if data_map[y][x] ==1 and visit_chk[y][x] == False:
            visit_chk[y][x] = True
            # 그림카운트 1
            img_cnt += 1
            maxv = max(maxv, bfs(y, x))


print(img_cnt)
print(maxv)