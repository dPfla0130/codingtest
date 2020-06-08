from collections import deque
import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

board =[list(map(int, input())) for _ in range(n)]
chk = [[[-1]*2 for _ in range(m)] for _ in range(n)]

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
                if board[nx][ny]==0 and chk[nx][ny][z]==-1:
                    chk[nx][ny][z] = chk[x][y][z]+1
                    q.append([nx, ny, z])
                if z==0 and board[nx][ny]==1 and chk[nx][ny][z+1]==-1:
                    chk[nx][ny][z+1] = chk[x][y][z]+1
                    q.append([nx, ny, z+1])


BFS()
an1 , an2 = chk[n-1][m-1][0], chk[n-1][m-1][1]

if an1==-1 and an2 !=-1:
    print(an2)
elif an1!=-1 and an2==-1:
    print(an1)
else:
    print(min(an1, an2))
