from sys import stdin

N = int(stdin.readline())
confs = []
for i in range(N):
    s, e = map(int, stdin.readline().split())
    confs.append((s, 1))
    confs.append((e, -1))
confs.sort(key=lambda x : (x[0], x[1]))

maxroom = 0
room = 0
for time, n in confs:
    room+=n
    if room>maxroom: maxroom=room

print(maxroom)