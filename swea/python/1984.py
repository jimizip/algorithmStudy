T = int(input())
for test_case in range(1, T+1):
    num_list = list(map(int, input().split()))
    min_num = min(num_list)
    max_num = max(num_list)
    num_list.remove(min_num)
    num_list.remove(max_num)
    print(f'#{test_case} {round(sum(num_list) / 8)}')