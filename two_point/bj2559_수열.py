"""
1. 문제 
https://www.acmicpc.net/problem/2559

2.아이디어
숫자를 반복문으로 돌면서 결과의 최대값을 구함

3. 시간복잡도 
-for : N = 100000
-각 위치에 k개의 값 더함 : k = 100000
-총 N * K = 100억

4. 자료구조
- 입력받은 온도 배열 : int[]
- 최대값 변수
- 연속된 수 저장 배열 : int[]

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
max_v = None
sum_data = 0
cnt = 0

for i in range(n):
    sum_data += data[i]
    cnt += 1
    if cnt == k:
        check_data =sum_data

        if max_v == None:
            max_v = check_data
        else:
            if max_v < check_data:
                max_v = check_data

        sum_data = sum_data - data[i-(k-1)]
        cnt = cnt-1

print(max_v)
