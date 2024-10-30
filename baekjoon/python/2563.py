N = int(input())
result = 0 
arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())

    for row in range(x, x+10):
        for col in range(y, y+10):
            arr[row][col] = 1

for i in arr:
    result += sum(i)

print(result)