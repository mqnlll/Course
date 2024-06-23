n,m=map(int,input().split())
arr=[]
for _ in range(m):
    u,v,c = map(int,input().split())
    arr.append((c,u,v))
arr.sort()
fa=[i for i in range(n+1)]
def get_fa(x):
    if fa[x] == x:
        return x
    fa[x] = get_fa(fa[x])
    return fa[x]
index = 0
cnt = 0
while 1:
    c,u,v = arr[index]
    if get_fa(u) != get_fa(v):
        fa[get_fa(u)] = get_fa(v)
        cnt += 1
        if cnt==n-1:
            print(cnt,c)
            break
    index+=1