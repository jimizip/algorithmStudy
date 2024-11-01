N, B = map(int, input().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while N:
    result += arr[N%B]
    N //= B

print(result)

