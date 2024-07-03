"""
문제 
https://www.acmicpc.net/problem/2309

1. 알고리즘
- 난장이 9마리의 키를 배열로 선택하여 중복되지 않는 7개를 추출하여 만약 합이 100이면 해당 리스트를 출력

2. 시간복잡도
백트래킹을 사용하여 처리

3. 자료구조
- 난장이 리스트 -=int[]
- 결과저장 = int[]


"""


import sys
input = sys.stdin.readline

exit_code = 0
data = [int(input().strip()) for _ in range(9)]
chk = [False] * 9
rs = []

def sum_key():
    global rs
    sum_key_rs = 0
    for i in rs:
        sum_key_rs += data[i]

    return sum_key_rs


def recure(num):
    global exit_code
    if len(rs) == 7:
 
        sum_key_rs = sum(rs)
        if sum_key_rs == 100:
            exit_code = -1
        return

    for i in range(9):
        if chk[i] == False:
            chk[i] = True
            rs.append(data[i])
            recure(num+1)
            if exit_code == -1:
                return
            rs.pop()
            chk[i] = False

recure(0)
rs.sort()
for i in rs:
    print(i)