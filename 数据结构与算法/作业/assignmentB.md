# Assignment #B: 图论和树算

Updated 1709 GMT+8 Apr 28, 2024

2024 spring, Complied by 陈涛 经济学院==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：vscode,python3.10

C/C++编程环境：vs2022



## 1. 题目

### 28170: 算鹰

dfs, http://cs101.openjudge.cn/practice/28170/



思路：



代码

```python
# 
dire=[(-1,0),(1,0),(0,-1),(0,1)]
graph=[input() for _ in range(10)]
ans=0
vis=[[0]*10 for _ in range(10)]
def dfs(x,y):
    if x<0 or x>9 or y<0 or y>9:
        return
    if graph[x][y]=='-':
        return
    if vis[x][y]:
        return
    vis[x][y]=1
    for d in dire:
        dfs(x+d[0],y+d[1])
for i in range(10):
    for j in range(10):
        if graph[i][j]=='.'  and not vis[i][j]:
            ans+=1
            dfs(i,j)
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-02 210857.png"></img>


### 02754: 八皇后

dfs, http://cs101.openjudge.cn/practice/02754/



思路：



代码

```python
# 
board=[[0]*8 for i in range(8)]
result=[]
r=[]
def check(x,y):
    for i in range(x):
        if board[i][y]==1:
            return 0
    for d in range(1,min(x,y)+1):
        if board[x-d][y-d]==1:
            return 0
    for d in range(1,min(x,7-y)+1):
        if board[x-d][y+d]==1:
            return 0
    return 1
def dfs(depth):
    if depth==8:
        result.append(''.join(r))
        return
    for i in range(8):
        if check(depth,i):
            r.append(str(i+1))
            board[depth][i]=1
            dfs(depth+1)
            r.pop()
            board[depth][i]=0
dfs(0)
result.sort()
n=int(input())
for _ in range(n):
    print(result[int(input())-1])
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-02 214715.png"></img>


### 03151: Pots

bfs, http://cs101.openjudge.cn/practice/03151/



思路：



代码

```python
# 
from collections import deque
ops=['FILL(1)','FILL(2)','DROP(1)','DROP(2)','POUR(2,1)','POUR(1,2)']
a,b,c=map(int,input().split())
def pour(i,now):
    if i==2:
        if now[0]+now[1]<=a:
            return (now[0]+now[1],0)
        else:
            return (a,now[1]-a+now[0])
    else:
        if now[0]+now[1]<=b:
            return (0,now[0]+now[1])
        else:
            return (now[1]-b+now[0],b)
q=deque()
now=(0,0,'')
vis=set()
res=''
while 1:
    if now[0]==c or now[1]==c:
        res=now[2]
        break
    if not (a,now[1]) in vis:
        vis.add((a,now[1]))
        q.append((a,now[1],now[2]+'0'))
    if not (now[0],b) in vis:
        vis.add((now[0],b))
        q.append((now[0],b,now[2]+'1'))
    if not (0,now[1]) in vis:
        vis.add((0,now[1]))
        q.append((0,now[1],now[2]+'2'))
    if not (now[0],0) in vis:
        vis.add((now[0],0))
        q.append((now[0],0,now[2]+'3'))
    tmp=pour(2,now)
    if not tmp in vis:
        vis.add(tmp)
        q.append(tmp+(now[2]+'4',))
    tmp=pour(1,now)
    if not tmp in vis:
        vis.add(tmp)
        q.append(tmp+(now[2]+'5',))
    if not q:
        break
    now=q.popleft()
if res:
    print(len(res))
    for i in res:
        print(ops[int(i)])
else:
    print('impossible')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-02 214827.png"></img>


### 05907: 二叉树的操作

http://cs101.openjudge.cn/practice/05907/



思路：



代码

```python
# 
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    tree=[0]*n
    fa=[-1]*n
    def f(x):
        if tree[x][0]==-1:
            return x
        return f(tree[x][0])
    for i in range(n):
        x,y,z=map(int,input().split())
        tree[x]=[y,z]
        if y!=-1:
            fa[y]=x
        if z!=-1:
            fa[z]=x
    for i in range(m):
        inp=input().split()
        if inp[0]=='1':
            x,y=map(int,inp[1:3])
            fax,fay=fa[x],fa[y]
            tmpx=tree[fax][:]
            tmpy=tree[fay][:]
            tree[fax][tmpx.index(x)]=y
            tree[fay][tmpy.index(y)]=x
            fa[x],fa[y]=fay,fax
        else:
            x=int(inp[1])
            print(f(x))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-02 222007.png"></img>



### 18250: 冰阔落 I

Disjoint set, http://cs101.openjudge.cn/practice/18250/



思路：



代码

```python
# 
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
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-02 222107.png"></img>

### 05443: 兔子与樱花

http://cs101.openjudge.cn/practice/05443/



思路：



代码

```python
# 
import heapq
p=int(input())
g={}
locs=[]
locsn={}
for i in range(p):
    locs.append(input())
    locsn[locs[-1]]=i
    g[i]=[]
mat=[[0]*p for _ in range(p)]
q=int(input())
for _ in range(q):
    s,e,l=input().split()
    g[locsn[s]].append((int(l),locsn[e]))
    g[locsn[e]].append((int(l),locsn[s]))
    mat[locsn[s]][locsn[e]]=int(l)
    mat[locsn[e]][locsn[s]]=int(l)
def dij(s,e):
    qe=[]
    vis=[0]*p
    now=(0,s,[s])
    vis[s]=1
    while 1:
        node=now[1]
        if node==e:
            return now[2]
        base=now[0]
        path=now[2]
        for edge in g[node]:
            if not vis[edge[1]]:
                path.append(edge[1])
                heapq.heappush(qe,(edge[0]+base,edge[1],path[:]))
                path.pop()
        while 1:
            tmp=heapq.heappop(qe)
            if not vis[tmp[1]]:
                vis[tmp[1]]=1
                now=tmp
                break
r=int(input())
for _ in range(r):
    s,e=input().split()
    if(s==e):
        print(s)
        continue
    path=dij(locsn[s],locsn[e])
    out=''
    for i in range(len(path)-1):
        out+=locs[int(path[i])]+'->'+f'({mat[path[i]][path[i+1]]})->'
    out+=locs[int(path[-1])]
    print(out)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-02 222234.png"></img>



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

五一去玩了QAQ, 有在跟每日选做，除了Saving Tang Monk



