import sys
from collections import deque
n= int(input())
board = [list(map(str, input())) for _ in range(n)]
board2 = [['']*n for _ in range(n)]
chk = [[0]*n for _ in range(n)]
chk2 = [[0]*n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()

def BFS(x, y, c):
    q.append((x, y, c))
    chk[x][y]=1
    global cnt

    while(q):
        tmp = q.pop()
        tx = tmp[0]
        ty = tmp[1]
        tc = tmp[2]
        for i in range(4):
            nx = tx+dx[i]
            ny = ty+dy[i]
            if 0<=nx<n and 0<=ny<n and chk[nx][ny]==0 and tc==board[nx][ny]:
                q.append((nx, ny, board[nx][ny]))
                chk[nx][ny]=1
    cnt+=1

def BFS_RG(x, y, c):
    q.append((x, y, c))
    chk2[x][y]=1
    global cnt

    while(q):
        tmp = q.pop()
        tx = tmp[0]
        ty = tmp[1]
        tc = tmp[2]
        for i in range(4):
            nx = tx+dx[i]
            ny = ty+dy[i]
            if 0<=nx<n and 0<=ny<n and chk2[nx][ny]==0 and tc==board2[nx][ny]:
                q.append((nx, ny, board2[nx][ny]))
                chk2[nx][ny]=1
    cnt+=1


if __name__=="__main__":
    cnt=0

    for i in range(n):
        for j in range(n):
            if chk[i][j]==0:
                BFS(i, j, board[i][j])
            if board[i][j]=='G':
                board2[i][j]='R'
            else:
                board2[i][j]=board[i][j]
    print(cnt, end=' ')

    cnt=0

    for i in range(n):
        for j in range(n):
            if chk2[i][j]==0:
                BFS_RG(i, j, board2[i][j])
    print(cnt)
