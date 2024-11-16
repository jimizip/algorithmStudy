T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    day_list = list(map(int, input().split()))
    if len(day_list) != N:
        break
    max_num = 0
    profit = 0
    for i in reversed(day_list):
        if i > max_num:
            max_num = i
        else:
            profit += max_num - i
    print(f'#{test_case} {profit}')