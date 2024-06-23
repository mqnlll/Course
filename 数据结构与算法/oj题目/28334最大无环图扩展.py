from collections import deque
n,m=map(int,input().split())
g=[[] for _ in range(n)]
degree = [0]*n
for _ in range(m):
    a,b=map(int,input().split())
    if not b in g[a]:
        g[a].append(b)
        degree[b] += 1
now = -1
q = deque()
for i in range(n):
    if degree[i] == 0:
        q.append(i)
if q:
    now=q.popleft()
tps = []
k = 0
if now !=-1:
    tps.append(now)
    while 1:
        for nx in g[now]:
            degree[nx]-=1
            if degree[nx] ==0:
                q.append(nx)
        if not q:
            break
        now = q.popleft()
        tps.append(now)
if len(tps)==n:
    for i in range(n):
        for j in range(i+1,n):
            if not tps[j] in g[tps[i]]:
                k+=1
print(k)