import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**8)
test_case = int(sys.stdin.readline())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 1:
            board[nx][ny] = 0
            DFS(nx, ny)
    return

for i in range(test_case):
    m, n, t = tuple(map(int, sys.stdin.readline().split()))
    board = [[0] * n for _ in range(m)]
    cnt = 0

    for j in range(t):
        x, y = map(int, sys.stdin.readline().split())
        board[x][y] = 1


    for k in range(m):
        for p in range(n):
            if board[k][p]==1:
                cnt += 1
                DFS(k, p)
    print(cnt)














