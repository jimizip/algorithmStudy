T = int(input())
for test_case in range(1, T+1):
    t = int(input())
    if test_case != t:
        break
    scores = list(map(int, input().split()))
    cnt = dict()
    for i in scores:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    
    max_cnt = max(cnt.values())
    result = []
    for i in cnt:
        if cnt[i] == max_cnt:
            result.append(i)
    result.sort(reverse=True)
    print(f'#{test_case} {result[0]}')