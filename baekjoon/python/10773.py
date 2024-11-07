K = int(input())

num = []
for i in range(K):
    n = int(input())
    if n == 0:
        if num:
            num.pop()
    else:
        num.append(n)

print(sum(num))