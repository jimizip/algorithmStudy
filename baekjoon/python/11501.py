import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    day_list = list(map(int, input().split()))
    max_num = 0
    profit = 0
    for i in reversed(day_list):
        if i > max_num:
            max_num = i
        else:
            profit += max_num - i
    print(profit)