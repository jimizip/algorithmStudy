# 메모리:114936KB, 시간: 328ms

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
empty = []
virus = []

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(M):
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    que = deque(virus)
    visited = [[0] * M for _ in range(N)]
    count = len(empty) - 3

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                que.append((nx, ny))
                count -= 1

    return count

result = 0
for walls in combinations(empty, 3):
    for x, y in walls:
        graph[x][y] = 1
    
    result = max(result, bfs())
    
    for x, y in walls:
        graph[x][y] = 0

print(result)


# 메모리: 121976KB, 시간: 2272ms
# import sys, copy
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs():
#     global result
#     que = deque()
#     temp_graph = copy.deepcopy(graph)

#     for i in range(N):
#         for j in range(M):
#             if temp_graph[i][j] == 2:
#                 que.append((i, j))
    
#     while que:
#         x, y = que.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
            
#             if temp_graph[nx][ny] == 0:
#                 temp_graph[nx][ny] = 2
#                 que.append((nx, ny))
        
#     cnt = 0

#     for i in range(N):
#         cnt += temp_graph[i].count(0)
    
#     result = max(result, cnt)

# def wall(cnt):
#     if cnt == 3:
#         bfs()
#         return
    
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 wall(cnt+1)
#                 graph[i][j] = 0



# result = 0
# wall(0)
# print(result)


