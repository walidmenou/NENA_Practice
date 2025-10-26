import sys
from collections import defaultdict, deque

n, m = [int(x) for x in sys.stdin.readline().strip().split()]
adj = defaultdict(list)

stations = set()
for i in range(m):
    a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    adj[a].append(b)
    stations.add(a)
    stations.add(b)

start1, start2 = [int(x) for x in sys.stdin.readline().strip().split()]

visited1 = set([start1])
visited2 = set([start2])

q = deque([(start1, 1), (start2, 2)])

res = -1

while q:
    cur, who = q.popleft()
    for i in adj[cur]:
        if who == 1 and i in visited2 or who == 2 and i in visited1:
            res = i
            break
        if who == 1 and i not in visited1:
            visited1.add(i)
            q.append((i, who))
        if who == 2 and i not in visited2:
            visited2.add(i)
            q.append((i, who))
    if res != -1:
        break

if res == -1:
    print('no')
else:
    print('yes')
    print(res)
