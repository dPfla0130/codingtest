import sys
sys.stdin = open("input.txt", "rt")

num1, num2 = map(int, input().split())
n1 = list(input())
n2 = list(input())
t = int(input())
n1.reverse()

result = ['']*(num1+num2)
ans = ''

if t>=num1+num2:
    for i in n2:
        ans+=i
    for i in n1:
        ans+=i
    print(ans, end='')
    exit(1)

for i in range(num2):
    if t-i<0:
        result[i+num1] = n2[i]
    else:
        if i+num1-(t-i) > 0:
            result[i + num1 - (t - i)] = n2[i]
        else:
            result[i] = n2[i]

c =0
i=0

while i<num1:
    if result[c]=='':
        result[c] = n1[i]
        i+=1
    c+=1
for i in result:
    ans+=i
print(ans, end='')