n=int(input())
height=list(map(int,input().split()))
left=[0]*(n+2)
right=[0]*(n+2)
for i in range(1,n+1):
    left[i]=max(left[i-1],height[i-1])
for i in range(n,0,-1):
    right[i]=max(right[i+1],height[i-1])
ans=0
for i in range(1,n+1):
    ans+=max(0,min(left[i-1],right[i+1])-height[i-1])
print(ans)