T = int(input())
for test_case in range(1, T+1):
    str_in = list(input())
    print(str_in)
    print(str_in[:-1])
    if str_in == str_in[::-1]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')