import sys

sys.stdin = open("input.txt", "rt")
num = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = []

s = 0
for i in arr:
    s += i
    result.append(s)

print(sum(result))





