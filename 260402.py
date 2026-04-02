# 나무 자르기
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

height = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for t in trees:
        if t > mid:
           cnt += (t - mid)

    if cnt >= M:
        height = mid
        start = mid + 1

    else:
        end = mid - 1

print(height)