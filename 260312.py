# 다리 만들기 2 
def dfs(connected, cost):
    global cnt, min_res

    if len(connected) == cnt:
        min_res = min(min_res, cost)
        return

    for c in list(connected):
        for distance, v in graph[c]:
            if v not in connected:
                connected.add(v)
                dfs(connected, cost + distance)
                connected.remove(v)


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
idx = 1
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1 and visited[i][j] == 0:
            stack = [(i, j)]
            visited[i][j] = idx
            while stack:
                r, c = stack.pop()
                for dr, dc in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                        if maps[nr][nc] == 1:
                            stack.append((nr, nc))
                            visited[nr][nc] = idx
            idx += 1

graph = [[] for _ in range(idx)]

for a in range(N):
    for b in range(M):
        if visited[a][b] != 0:
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                cur_i, cur_j = a + di, b + dj
                dist = 0
                while True:
                    if 0 <= cur_i < N and 0 <= cur_j < M:

                        if visited[cur_i][cur_j] == visited[a][b]:
                            break

                        elif visited[cur_i][cur_j] == 0:
                            cur_i += di
                            cur_j += dj
                            dist += 1
                        else:
                            if dist >= 2:
                                if visited[cur_i][cur_j] != 0 and (dist, visited[cur_i][cur_j]) not in graph[visited[a][b]]:
                                    graph[visited[a][b]].append((dist, visited[cur_i][cur_j]))
                            break

                    else:
                        break

for g in graph:
    g.sort(key = lambda x: x[0])

cnt = idx - 1
min_res = float('inf')
start = {1}
dfs(start, 0)

if min_res == float('inf'):
    print(-1)
else:
    print(min_res)





