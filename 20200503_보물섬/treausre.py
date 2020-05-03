import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
m, n = map(int, input().split())
board = [list(map(str, input())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()


def BFS(x, y):
    dis = 0
    q.append((x, y, 0))
    chk[x][y] = 1
    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0]+dx[i]
            ny = tmp[1]+dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if board[nx][ny] == 'L' and chk[nx][ny] == 0:
                q.append((nx, ny, tmp[2]+1))
                chk[nx][ny] = 1
                dis = tmp[2]+1

    return dis

if __name__ == '__main__':
    max_dis = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'L':
                chk = [[0] * n for _ in range(m)]
                max_dis = max(max_dis, BFS(i, j))
    print(max_dis)







