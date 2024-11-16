import sys
input = sys.stdin.readline

def count_max(board):
    N = len(board)
    answer = 1

    for i in range(N):  # 행에서
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)
    
    for i in range(N):  # 열에서
        cnt = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)
    
    return answer

N = int(input())
board = [list(input().strip()) for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        if j+1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, count_max(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
        if i+1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, count_max(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)