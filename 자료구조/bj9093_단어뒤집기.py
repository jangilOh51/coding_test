"""
1. 문제 
https://www.acmicpc.net/problem/9093

2. 아이디어 
- 단어별로 배열에 저장하여 하나식 뒤집어서 print한다.

3. 시간복잡도
 - 1000 * T
 t의 갯수를 알수 없어서 정확히 알기 어려움

 4. 자료구조
 이중배열로 저장해서 단어를 뒤집기 : str[][]

"""

import sys

input = sys.stdin.readline

T = int(input())

line_list = [input().split() for _ in range(T)]

# print(word_list)


for i in range(T):
    rs_line =""
    line = line_list[i]
    word_cnt = len(line)
    for j in range(word_cnt):
        word = line[j]
        word_size = len(word)
        for k in range(word_size):
            rs_line += word[word_size -1 - k]

        if (word_cnt -1) != j:
            rs_line +=" "
    print(rs_line)

        
