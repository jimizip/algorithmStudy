import sys
imput = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))

min_num = num_list[0]
max_result = 0

for i in num_list[1:]:
    max_result = max(max_result, i - min_num)
    min_num = min(min_num, i)

print(max_result)