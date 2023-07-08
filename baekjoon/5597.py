s_list = [i for i in range(1, 31)]

for i in range(28):
    n = int(input())
    s_list.remove(n)

print(min(s_list))
print(max(s_list))