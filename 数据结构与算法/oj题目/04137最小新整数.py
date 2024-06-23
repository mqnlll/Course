t=int(input())
for _ in range(t):
    n,k=input().split()
    n=list(n)
    k=int(k)
    loc=0
    while 1:
        try:
            if k==0:
                break
            if n[loc+1]<n[loc]:
                n.pop(loc)
                if loc>0:
                    loc-=1
                k-=1
            else:
                loc+=1
        except:
            break
    for i in range(k):
        n.pop()
    print(''.join(n))