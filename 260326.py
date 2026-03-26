# 스카이라인 쉬운거
N = int(input())
stack = []
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())

    # 1. 현재 높이(b)보다 높은 이전 건물들은 먼저 다 빼줍니다. (elif가 아닌 독립된 if/while문으로 분리)
    while stack and stack[-1] > b:
        stack.pop()

    # 2. 다 빼고 난 뒤, 스택이 비어있거나 스택의 최고점보다 b가 높을 때만 스택에 넣고 카운트합니다.
    if b > 0 and (not stack or stack[-1] < b):
        stack.append(b)
        cnt += 1

# 3. 스택에 들어갈 때 이미 모두 카운트했으므로, cnt += len(stack)은 삭제합니다!
print(cnt)