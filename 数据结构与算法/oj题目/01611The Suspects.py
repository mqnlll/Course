while 1:
    n,m=map(int,input().split())
    if n==0:
        break
    fa=[i for i in range(n)]
    def get_fa(x):
        if fa[x]==x:
            return x
        fa[x]=get_fa(fa[x])
        return fa[x]
    for _ in range(m):
        inp=list(map(int,input().split()))
        head=get_fa(inp[1])
        for i in range(2,inp[0]+1):
            if get_fa(inp[i])==0:
                head=0
                break
        for i in range(1,inp[0]+1):
            fa[get_fa(inp[i])]=head
    ans=0
    for i in range(n):
        if get_fa(i)==0:
            ans+=1
    print(ans)