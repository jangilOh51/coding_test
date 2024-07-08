"""
1. 문제
https://www.acmicpc.net/problem/10828

2. 아이디어 
- 각 명령을 저장하여 각 명령어별로 처리한다. 

3. 시간복잡도
- O(N) = 100000

4.자료구조
- stack 배열 : int[]
- 명령어 저장 배열 : arr_cmd[]


"""

import sys

input = sys.stdin.readline

N = int(input())

arr_cmd = [input().strip() for _ in range(N)]
# print(f"arr_cmd:{arr_cmd}")
stack = []


def excute_cmd(cmd:str):
    # print(f"cmd:{cmd}")
    if cmd == "top":
        # print(f"top:{cmd}")
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    
    if cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    if cmd == "size":
        print(len(stack))
    
    if cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if "push" in cmd:
        stack.append(cmd.split()[1])


for cmd in arr_cmd:
    excute_cmd(cmd)
