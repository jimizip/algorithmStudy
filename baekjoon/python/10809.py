import string

lower = [i for i in string.ascii_lowercase]
S = input()
for i in lower:
    print(S.find(i), end=" ")
    