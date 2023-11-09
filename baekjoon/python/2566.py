import sys
max_num = 0
row, col = 0, 0

for i in range(9):
    num_table = list(map(int, sys.stdin.readline().split()))
    if max_num < max(num_table):
        max_num = max(num_table)
        row = i
        col = num_table.index(max(num_table))

print(max_num)
print(row+1, col+1)