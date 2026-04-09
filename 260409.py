# 프로세서 연결하기
def dfs(idx, res, connected):
    global min_res, max_connected

    if idx == len(pro):
        if connected > max_connected:
            max_connected = connected
            min_res = res
        elif connected == max_connected:
            min_res = min(min_res, res)
        return

    if (len(pro) - idx) + connected < max_connected:
        return

    r, c = pro[idx]
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        path = []
        nr, nc = r, c
        possible = False
        while True:
            nr += dr
            nc += dc
            if not (0 <= nr < N and 0 <= nc < N):
                possible = True
                break
            if visited[nr][nc]:
                break
            path.append((nr, nc))

        if possible:
            for a, b in path:
                visited[a][b] = True
            dfs(idx + 1, res + len(path), connected + 1)
            for a, b in path:
                visited[a][b] = False

    dfs(idx + 1, res, connected)

T = int(input())
for t in range(T):
    N = int(input())
    maxinos = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    pro = []
    for i in range(N):
        for j in range(N):
            if maxinos[i][j] == 1:
                visited[i][j] = True
                if 0 < i < N - 1 and 0 < j < N - 1:
                    pro.append((i, j))

    min_res = float('inf')
    max_connected = 0
    dfs(0, 0, 0)
    print(f'#{t + 1} {min_res}')