# 처음 짠 코드
H,M = map(int, input().split())
if H != 0 and M == 0:
    H = H - 1
    M = M + 15
    print(H, M)
elif H == 0 and M == 0:
    H = H +23
    M = M + 15
    print(H, M)
elif H != 0 and M != 0:
    if M < 45:
        H = H -1
        T = 45 - M
        M = 60 - T
    else:
        M = M - 45
    print(H, M)
elif H == 0 and M != 0:
    if M < 45:
        H = H + 23
        T = 45 - M
        M = 60 - T
    else:
        M = M - 45
    print(H, M)


# 다른 코드
hour, min = map(int,input().split())

if min >= 45:
    print(hour, min-45)
elif hour>0 and min < 45:
    print(hour-1, min+15)
else:
    print(23, min+15)