import sys
sys.stdin = open("input.txt", "rt")

from collections import deque
li = list(map(int, input().split()))
n = li[0]
m = li[1]
k = li[2]

board =[list(map(int, input())) for _ in range(n)]
chk = [[[-1]*(k+1) for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

def BFS():

    #(x, y, 벽을 부술 수 있는 횟수)
    q.append([0, 0, 0])
    chk[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                #방문하지 않았고, 벽이 없는 곳으로 이동
                if board[nx][ny]==0 and chk[nx][ny][z]==-1:
                    chk[nx][ny][z] = chk[x][y][z]+1
                    q.append([nx, ny, z])
                ##벽을 부수는 횟수가 남았고, 벽을 부수려하는데 동시에 방문하지 않았을 때
                elif z<k and board[nx][ny]==1 and chk[nx][ny][z+1]==-1:
                    #벽을 부쉈고, 방문한다
                    chk[nx][ny][z+1] = chk[x][y][z]+1
                    q.append([nx, ny, z+1])


BFS()

min = 9999999
for i in range(k+1):
    if chk[n-1][m-1][i]< min and chk[n-1][m-1][i] != -1:
        min = chk[n-1][m-1][i]

if min==9999999:
    print(-1)
else:
    print(min)