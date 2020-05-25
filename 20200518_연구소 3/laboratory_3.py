import sys
from collections import deque
import copy
from itertools import combinations

sys.stdin = open("input.txt", "rt")
tmp = list(map(int, input().split()))
n = tmp[0]
vn = tmp[1]
board = [list(map(int, input().split())) for _ in range(n)]
tmp = copy.deepcopy(board)
chk = [[0]*n for _ in range(n)]
virus = []
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
mb = [[99999] * n for _ in range(n)]

def BFS():
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and chk[nx][ny]==0 and board[nx][ny]==0:
                q.append((nx, ny))
                chk[nx][ny] = 1
                board[nx][ny] = board[x][y] + 1

def max_dis():
    m = 0
    for i in range(n):
        m = max(max(board[i]), m)
    return m

def chk_virus(ch_v):
    for i in range(n):
        for j in range(n):
            if ([i, j]) not in ch_v and board[i][j]==0:
                return False
    return True

def chk_board():
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                return True
    return False

if __name__=='__main__':
    if chk_board() == False:
        print(0)
        exit(0)
    answer = 9999
    un_virus=[]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                virus.append([i, j])
    ch_v = list(combinations(virus, vn))

    for i in range(len(ch_v)):
        for j in range(len(virus)):
            if virus[j] not in ch_v[i]:
                un_virus.append(virus[j])

        for j in range(len(un_virus)):
            board[un_virus[j][0]][un_virus[j][1]] = 0

        for j in range(vn):
            x = ch_v[i][j][0]
            y = ch_v[i][j][1]
            board[x][y] = 0
            q.append((x, y))
            chk[x][y] = 1
        BFS()
        for j in range(len(un_virus)):
            board[un_virus[j][0]][un_virus[j][1]] = 1
        if chk_virus(ch_v[i]):
            answer = min(max_dis(), answer)
        un_virus.clear()
        board = copy.deepcopy(tmp)
        chk = [[0]*n for _ in range(n)]
    if answer == 9999:
        answer = -1
    print(answer)








