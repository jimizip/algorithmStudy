base_list = [1, 1, 2, 2, 2, 8]
input = list(map(int, input().split()))

for i in range(len(base_list)):
    print(base_list[i]-input[i], end=" ")