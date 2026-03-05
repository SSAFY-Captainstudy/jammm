# 탈주범 검거
 
from collections import deque
 
 
def is_connected(r, c):
    global dr, dc
    for ndr, ndc in dir_dict[maps[r][c]]:
        if dr + ndr == 0 and dc + ndc == 0:
            return True
    return False
 
 
T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
 
    dir_dict = { 1 : [[1, 0], [0, -1], [-1, 0], [0, 1]],
                 2 : [[1, 0], [-1, 0]],
                 3 : [[0, -1], [0, 1]],
                 4 : [[-1 ,0], [0, 1]],
                 5 : [[1, 0], [0, 1]],
                 6 : [[1, 0], [0, -1]],
                 7 : [[-1, 0], [0, -1]]
                 }
 
    deq = deque([(R, C, 1)])
    visited[R][C] = True
 
 
    while deq:
        cur_r, cur_c, cur_t = deq.popleft()
        cur_dir = dir_dict[maps[cur_r][cur_c]]
 
        if cur_t == L:
            break
 
        for dr, dc in cur_dir:
            nr, nc = cur_r + dr, cur_c +dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if maps[nr][nc] != 0 and is_connected(nr, nc):
                    deq.append((nr, nc, cur_t + 1))
                    visited[nr][nc] = True
 
    cnt = 0
    for n in range(N):
        for m in range(M):
            if visited[n][m]:
                cnt += 1
 
    print(f'#{t+1} {cnt}')