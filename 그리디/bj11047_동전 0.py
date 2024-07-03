"""
1. 문제 
https://www.acmicpc.net/problem/11047

2. 아이디어
- 동전수를 큰수부터 정렬한다.
- for문돌면서 큰수부터 나누어서 몫이 1이상이면 갯수로 하고 나머지를 순서대로 대입하여 떨어지는 수로 구한다.

3. 시간복잡도
for : N> O(N)

4. 자료구조
- n, k를 정수로 받는다.
- 동전수를 배열로 저장한다.  

"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
won_list = [int(input()) for _ in range(n)]
won_list.sort(reverse=True)

cnt = 0
for i in won_list:
    i_cnt = k//i
    if i_cnt >=1:
        cnt += i_cnt
        k = k%i

print(cnt)