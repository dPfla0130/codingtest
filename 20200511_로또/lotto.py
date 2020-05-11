import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방

# 조합을 이용한 숫자 뽑기
def DFS(start, L):
    tmp = arr[1:]
    if len(result)==6:
        for k in range(len(result)):
            print(result[k], end=' ')
        print()
        return
    for i in range(start, len(tmp)): #현재 위치 start 변수 필요, 0부터 시작하면 순열
        if chk[i]==0:
            result.append(tmp[i])
            chk[i]=1
            DFS(i, L+1)
            chk[i]=0
            result.pop()

while True:
    arr = list(map(int, input().split()))
    if arr[0]==0:
        break
    chk = [0] * arr[0]
    result = []

    DFS(0, 0)
    print()




