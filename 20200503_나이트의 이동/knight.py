import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
test_case = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def BFS(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy))
    board[sx][sy] = 1

    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return board[x][y]-1
        for j in range(8):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0<=nx<l and 0<=ny<l and board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] = board[x][y]+1

for i in range(test_case):
    l = int(input())
    board = [[0]*l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx==ex and sy==ey:
        print(0)
        continue
    print(BFS(sx, sy, ex, ey))














