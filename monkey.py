import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")
k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
chk = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
#말 이동 좌표
dhx = [-2, -1, 1, 2, 2, 1, -1, -2]
dhy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

def BFS(x, y, z):
    
    q.append((x, y, z))
    chk[x][y][z]=1
    

    while q:
        tmp = q.popleft()
        if tmp[0]==h-1 and tmp[1]==w-1:
            print(chk[tmp[0]][tmp[1]][tmp[2]]-1)
            return

        if tmp[2]<k:
            horse(tmp[0], tmp[1], tmp[2])
            monkey(tmp[0], tmp[1], tmp[2])
        elif tmp[2]==k:
            monkey(tmp[0], tmp[1], tmp[2])
    print(-1)
        

def horse(x, y, z):
    for i in range(8):
        hx = x+dhx[i]
        hy = y+dhy[i]
        if 0<=hx<h and 0<=hy<w and board[hx][hy]==0 and chk[hx][hy][z+1]==0:
            chk[hx][hy][z+1]=chk[x][y][z]+1
            q.append((hx, hy, z+1))
            

def monkey(x, y, z):
    for i in range(4):
            mx = x+dx[i]
            my = y+dy[i]
            if 0<=mx<h and 0<=my<w and board[mx][my]==0 and chk[mx][my][z]==0:
                chk[mx][my][z]=chk[x][y][z]+1
                q.append((mx,my,z))
                

if __name__=='__main__':
    
    BFS(0, 0, 0)
    


