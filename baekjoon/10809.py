import string

lower = [i for i in string.ascii_lowercase]
S = list(input())
for i in lower:
    if i in S:
        print(S.index(i), end=" ")
    else:
        print(-1, end=" ")

