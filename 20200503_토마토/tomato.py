from collections import deque

def bfs(q, answer):
    count = answer
    while q:
        tmp = q.popleft()
        x = tmp[0]
        y = tmp[1]
        cnt = tmp[2]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if tomato[nx][ny] == 0 and tomato[nx][ny] != -1:
                    tomato[nx][ny] = 1
                    q.append([nx, ny, cnt + 1])
    return cnt


def check(answer, tomato):
    for i in range(len(tomato)):
        for j in range(len(tomato[i])):
            if tomato[i][j] == 0:
                return -1
    return answer


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0
q = deque([])

for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        if tomato[i][j] == 1:
            q.append([i, j, answer])
answer = bfs(q, answer)

print(check(answer, tomato))



