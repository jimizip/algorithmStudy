import sys

N = int(input())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(num)/N))

# 중앙값
num.sort()
print(num[N//2])

# 최빈값
cnt = dict()
for i in num:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

mx = max(cnt.values())
mx_list = []

for i in cnt:
    if cnt[i] == mx:
        mx_list.append(i)

mx_list.sort()
if len(mx_list) == 1:
    print(mx_list[0])
else:
    print(mx_list[1])

# 범위
print(max(num)-min(num))