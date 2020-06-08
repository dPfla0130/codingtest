import sys
sys.stdin = open("input.txt", "rt")

num1, num2 = map(int, input().split())
import itertools
g1 = list(' '.join(list(input()[::-1])))
g2 = list(' '.join(list(input())))
T = int(input())

g2 = [' ']*len(g1)+g2+[' ']*len(g1)
g1 = [' ']*T*2+g1

for a in itertools.zip_longest(g1, g2, fillvalue=' '):
    a = ''.join(a).strip()
    if a:
        print(a, end='')