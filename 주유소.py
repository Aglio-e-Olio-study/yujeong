import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0
a = price[0]

for i in range(n-1):
    if price[i] < a:
        a = price[i]
    result += a * dist[i]

print(result)