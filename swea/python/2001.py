T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = list(map(int, input().strip()) for _ in range(N))
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for row in board[i:i+M]:
                result = sum(row[j:j+M])
        sum(result)
        kills = max(kills, result)
    
    print(kills)
