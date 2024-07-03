"""
1. 문제
https://www.acmicpc.net/problem/1920

2. 아이디어
- 처음받은 데이터 정렬
- 2번째 데이터 for문돌면서 첫번째 데이터 2진트리로 찾기 

3. 시간복잡도
- n정렬 : N
- 2진트리 검색 = m * lgN
= (N+M)* lgN = 20만 * 20 = 400만 < 2억

4. 자료구조
- n, m의 각각 저장하는 배열


"""

import sys
input = sys.stdin.readline

N = int(input())
data1 = list(map(int,input().split()))
M = int(input())
data2 = list(map(int,input().split()))

data1.sort()

def search(st:int, en:int, target):

    if st == en:
        if data1[st] == target:
            return True
        return False
    
    mid = (st+en)//2
    if data1[mid] < target:
        return search(mid+1, en, target)
    else:
        return search(st, mid, target)

for i in data2:
    if search(0,N-1, i):
        print(1)
    else:
        print(0)
