import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방

sys.stdin = open("input.txt", "rt")
testcase = int(input())

# 팀 선택하기
def DFS(L):

    chk[L]=1
    result.append(L)
    if chk[arr[L]-1]==0:
        DFS(arr[L]-1)
    else:
        if arr[L]-1 in result:
            n = result.index(arr[L]-1)

            for _ in range(n):
                result.pop(0)
        else:
            result.clear()


for i in range(testcase):
    num = int(input())
    arr = list(map(int, input().split()))
    chk = [0] * num
    term_pro = []
    for j in range(len(chk)):
        if chk[j] == 0:
            result = []
            DFS(j)
            num = num - len(result)
    print(num )

