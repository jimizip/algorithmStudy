array = []
for i in range(9):
    N = int(input())
    array.append(N)
print(max(array))
print(array.index(max(array))+1)