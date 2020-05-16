import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sys.stdin = open("input.txt", "rt")
R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]

def DFS(x, y, cnt):
    global ans
    global cur
    ans = max(ans, cnt)

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if board[nx][ny] not in cur:
                cur.append(board[nx][ny])
                DFS(nx, ny, cnt+1)
                cur.remove(board[nx][ny])


if __name__=="__main__":
    ans =0
    cur = []

    DFS(0, 0, ans)
    print(ans)


