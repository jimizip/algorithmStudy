num_list = []

for _ in range(10):
    A = int(input())
    if (A%42) not in num_list:
        num_list.append(A%42)

print(len(num_list))