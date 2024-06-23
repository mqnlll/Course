try:
    while 1:
        n,m=map(int,input().split())
        fa=[i for i in range(n+1)]
        def get_fa(x):
            if fa[x]==x:
                return x
            fa[x]=get_fa(fa[x])
            return fa[x]
        for _ in range(m):
            x,y=map(int,input().split())
            if get_fa(x)==get_fa(y):
                print('Yes')
            else:
                fa[get_fa(y)]=get_fa(x)
                print('No')
        cnt=0
        ans=[]
        for i in range(1,n+1):
            if get_fa(i)==i:
                ans.append(i)
                cnt+=1
        print(cnt)
        print(' '.join(map(str,ans)))
except:
    pass