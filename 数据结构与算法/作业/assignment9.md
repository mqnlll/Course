# Assignment #9: 图论：遍历，及 树算

Updated 1739 GMT+8 Apr 14, 2024

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

### 04081: 树的转换

http://cs101.openjudge.cn/dsapre/04081/



思路：



代码

```python
# 
s=input()
l=len(s)
i=-1
tree=[]
h1=0
def f(now,h):
    global i,h1
    while 1:
        i+=1
        if i==l:
            return
        if s[i]=='d':
            now.append([])
            f(now[-1],h+1)
        else:
            h1=max(h1,h)
            return
btree=[]
h2=0
def g(now,bnow,i,h):
    global h2
    if now[i]:
        bnow.append([])
        g(now[i],bnow[-1],0,h+1)
    if i+1<len(now):
        bnow.append([])
        g(now,bnow[-1],i+1,h+1)
    h2=max(h2,h)
f(tree,0)
g([tree],btree,0,0)
print(h1,'=>',h2)
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-17 170549.png"></img>


### 08581: 扩展二叉树

http://cs101.openjudge.cn/dsapre/08581/



思路：



代码

```python
# 
class node:
    def __init__(self,n) -> None:
        self.n=n
        self.l:node=None
        self.r:node=None
s=input()
i=0
def f(root):
    global i
    if i==len(s):
        return None
    if s[i]=='.':
        i+=1
        return None
    root=node(s[i])
    i+=1
    root.l=f(root.l)
    root.r=f(root.r)
    return root
ans=[]
def mid(root):
    if not root:
        return
    mid(root.l)
    ans.append(root.n)
    mid(root.r)
def suf(root):
    if not root:
        return
    suf(root.l)
    suf(root.r)
    ans.append(root.n)
root=f(None)
mid(root)
print(''.join(ans))
ans=[]
suf(root)
print(''.join(ans))
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-17 170729.png"></img>

### 22067: 快速堆猪

http://cs101.openjudge.cn/practice/22067/



思路：



代码

```python
# 
min_stack=[]
stack=[]
try:
    while 1:
        s=input().split()
        if s[0]=='push':
            n=int(s[1])
            stack.append(n)
            if min_stack:
                min_stack.append(min(n,min_stack[-1]))
            else:
                min_stack.append(n)
        else:
            if not stack:
                continue
            if s[0] == 'pop':
                stack.pop()
                min_stack.pop()
            else:
                print(min_stack[-1])
except:
    pass
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-17 172544.png"></img>


### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123



思路：



代码

```python
# 
t=int(input())
dire=[(2,-1),(2,1),(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2)]
for _ in range(t):
    n,m,x,y=map(int,input().split())
    vis=[[0]*m for _ in range(n)]
    cnt=0
    def dfs(x,y,depth):
        global cnt
        if x<0 or x>=n or y<0 or y>=m:
            return
        if vis[x][y]:
            return
        if depth==n*m:
            cnt+=1
            return
        vis[x][y]=1
        for d in dire:
            dfs(x+d[0],y+d[1],depth+1)
        vis[x][y]=0
    dfs(x,y,1)
    print(cnt)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-17 174151.png"></img>

### 28046: 词梯

bfs, http://cs101.openjudge.cn/practice/28046/



思路：



代码

```python
# 
from collections import deque
def get_buk(word):
    ans=[]
    for i in range(4):
        ans.append(word[:i]+'_'+word[i+1:])
    return ans
n=int(input())
words=[]
bucket={}
for i in range(n):
    s=input()
    words.append(s)
    buks=get_buk(s)
    for buk in buks:
        try:
            bucket[buk].append(i)
        except:
            bucket[buk]=[i]
graph=[0]*n
for i in range(n):
    graph[i]=[]
    buks=get_buk(words[i])
    for buk in buks:
        for w in bucket[buk]:
            if w!=i:
                graph[i].append(w)
sw,ew=input().split()
s=words.index(sw)
e=words.index(ew)
q=deque()
vis=[0]*n
now=(s,[s])
vis[s]=1
ans=[]
while 1:
    if now[0] == e:
        ans=now[1]
        break
    for w in graph[now[0]]:
        if not vis[w]:
            vis[w]=1
            q.append((w,now[1]+[w]))
    if not q:
        break
    now=q.popleft()
if ans:
    print(' '.join(map(lambda x:words[x],ans)))
else:
    print('NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-17 191926.png"></img>

### 28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/



思路：



代码

```python
# 
dire=[(2,-1),(2,1),(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2)]
n=int(input())
x,y=map(int,input().split())
vis=[[0]*n for _ in range(n)]
cnt=0
def count(x,y):
    count=0
    for d in dire:
        nx,ny=x+d[0],y+d[1]
        if 0<=nx<n and 0<=ny<n and not vis[nx][ny] :
            count+=1
    return count

def dfs(x,y,depth):
    global cnt
    if x<0 or x>=n or y<0 or y>=n:
        return
    if vis[x][y]:
        return
    if cnt:
        return
    if depth==n*n:
        cnt+=1
        return
    vis[x][y]=1
    next=[]
    for d in dire:
        next.append((count(x+d[0],y+d[1]),x+d[0],y+d[1]))
    next.sort()
    for k in next:
        dfs(k[1],k[2],depth+1)
    vis[x][y]=0
dfs(x,y,1)
print('success') if cnt else print('fail')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-17 205713.png"></img>


## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==


还是要善用python自带的dict，用好打表

学到了Warnsdorff’s 规则

