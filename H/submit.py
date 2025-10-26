import sys
from collections import defaultdict

n, m = [int(x) for x in sys.stdin.readline().strip().split()]
adj = defaultdict(list)

stations = set()
for i in range(m):
    a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    adj[a].append(b)
    stations.add(a)
    stations.add(b)

start1, start2 = [int(x) for x in sys.stdin.readline().strip().split()]


def reachable(n, t, seen):
    if n in seen:
        return False
    seen.add(n)

    if n == t:
        return True

    for i in adj[n]:
        if reachable(i, t, seen):
            return True
    return False


res = -1
for station in stations:
    seen1 = set()
    seen2 = set()
    if (reachable(start1, station, seen1)
            and reachable(start2, station, seen2)):
        res = station

if res != -1:
    print("yes")
    print(res)
else:
    print("no")
