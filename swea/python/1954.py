def snails(n):
    snail = [[0]*n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, d = 0, 0, 0

    for i in range(1, n*n+1):
        snail[x][y] = i
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny >= n or ny < 0 or snail[nx][ny] != 0:
            d = (d+1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        x, y = nx, ny

    return snail
        
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = snails(N)
    print(f'#{test_case}')
    for i in result:
        print(*i)
