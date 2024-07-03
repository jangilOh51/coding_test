"""
문제
https://www.acmicpc.net/problem/2667

1. 아이디어
- 이중포문으로 재귀로 돌면서 처리 DFS 로 재귀함수로 전역변수에서 카운트 한다

2. 시간복잡도 O = V + E
V = 25 * 25 = 625
E = 4 * 25 * 25 = 4 * 625 = 2500
복잡도는 =  625 + 2500 = 3125 < 2억 가능!!


3. 자료구조
- map_data = int[][]
- check = bool[][]
- edge = [] , []
- rs = [] 

"""


import sys

input = sys.stdin.readline

n = int(input())

map_data = [list(map(int,input().strip())) for _ in range(n)]

chk = [[False]*n for _ in range(n)]
rs = []

cnt = 0

dfs_x = [0,1,0,-1]
dfs_y = [1,0,-1,0]

def dfs(y, x):
    global cnt
    cnt +=1
    for i in range(4):
        dy = y + dfs_y[i]
        dx = x + dfs_x[i]

        if 0<=dy<n and 0<=dx<n:
            if map_data[dy][dx] ==1 and chk[dy][dx]==False:
                chk[dy][dx] = True
                dfs(dy,dx)
    



for y in range(n):
    for x in range(n):
        if map_data[y][x]==1 and chk[y][x] == False:
            cnt = 0

            chk[y][x]= True
            dfs(y, x)
            rs.append(cnt)


print(len(rs))
rs.sort()
for i in rs:
    print(i)

        
