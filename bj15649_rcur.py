"""
문제 : 
https://www.acmicpc.net/problem/15649

1. 아이디어 
- 백트래킹을 재귀함수에서 for문을 돌아서 숫자 선택(이전 방문확인)


2. 시간복잡도
- 숫자가 10이하여야 가능 8이라 가능

3. 자료구조
- rs = [] 수를 저장하는 변수
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
chk = [False]* (n+1)
rs = []

def recur(num):

    if num == m:
        print(" ".join(map(str,rs)))
        return
    
    for i in range(1, n+1):
        if chk[i]==False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            rs.pop()
            chk[i] = False


recur(0)
