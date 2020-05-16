import sys

sys.stdin = open("input.txt", "rt")
num = int(input())
arr = list(map(int, input().split()))

result = [0]*num
result[0] = arr[0]

for i in range(1, num):
#   result에는 지금까지의 최댓값만 저장되어있다
#   연속된 숫자의 합이므로, 현재 값이 지금까지 값보다 크다면, 연속된 숫자 끊어서 최대 값 갱신한다
#    print(arr[i], arr[i]+result[i-1])
    result[i] = max(arr[i], arr[i]+result[i-1])

#    print(result)

print(max(result))





