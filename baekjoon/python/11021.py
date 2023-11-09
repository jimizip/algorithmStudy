T = int(input())
N = 1
for i in range(T):
    A,B = map(int, input().split())
    print(f'Case #{N}: {A+B}')
    N += 1