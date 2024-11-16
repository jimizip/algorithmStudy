import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque([(x, y)])  # 수정: 튜플로 좌표 추가
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:  # 수정: N과 M의 순서 변경
                q.append((nx, ny))  # 수정: 튜플로 좌표 추가
                graph[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]  # 수정: N과 M의 순서 변경
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1  # 수정: x와 y의 순서 변경
    
    cnt = 0
    for i in range(N):  # 수정: 변수명 변경 및 범위 수정
        for j in range(M):  # 수정: 변수명 변경 및 범위 수정
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)