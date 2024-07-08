"""
1. 문제 
https://www.acmicpc.net/problem/11726

2. 아이디어 
- n 만큼 for 문을 돌면서 이전값만큼 더하기 
- n=1 : 1
- n=2 : 2
- n=3 : 3
- n=4 : 5
- n=5 : 8
= n= (n-1) + (n-2)

3. 시간복잡도
- O(N)

4. 자료구조
 이전값을 저장할 배열 : int[]
"""


import sys
input = sys.stdin.readline

n = int(input())
rs = [0,1,2]
for i in range(3,n+1):
    rs.append((rs[i-1]+ rs[i-2])%10007)

print(rs[n])