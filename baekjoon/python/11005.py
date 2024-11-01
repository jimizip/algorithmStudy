# N, B = map(int, input().split())
# arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# result = ""

# while N:
#     result += arr[N%B]
#     N //= B

# print(result[::-1])

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert(N, B):
    if N == 0:
        return "0"
    
    result = []
    while N:
        result.append(arr[N % B])
        N //= B
    
    return ''.join(result[::-1])

N, B = map(int, input().split())
print(convert(N, B))
