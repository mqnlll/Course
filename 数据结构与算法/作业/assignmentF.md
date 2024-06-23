# Assignment #F: All-Killed 满分

Updated 1844 GMT+8 May 20, 2024

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

### 22485: 升空的焰火，从侧面看

http://cs101.openjudge.cn/practice/22485/



思路：



代码

```python
# 
from collections import deque
n=int(input())
tree=[0]*(n+1)
for i in range(1,n+1):
    tree[i]=tuple(map(int,input().split()))
ans=[1]
q=deque()
now=(1,0)
while 1:
    if tree[now[0]][0]!=-1:
        q.append((tree[now[0]][0],now[1]+1))
    if tree[now[0]][1]!=-1:
        q.append((tree[now[0]][1],now[1]+1))
    if len(q)==0:
        break
    now = q.popleft()
    if len(q)==0:
        ans.append(now[0])
    elif q[0][1]>now[1]:
        ans.append(now[0])
print(' '.join(map(str,ans)))
```



代码运行截图 ==（至少包含有"Accepted"）==


<img src="./代码截图/屏幕截图 2024-05-21 135326.png"></img>


### 28203:【模板】单调栈

http://cs101.openjudge.cn/practice/28203/



思路：

甚至卡cin，cout

代码

```c++
#include <iostream>
#include <vector>
using namespace::std;

int arr[3000001];
int ans[3000001];

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }

    vector<int> down_stack;

    for (int i = n - 1; i >= 0; --i) {
        while (!down_stack.empty() && arr[down_stack.back()] <= arr[i]) {
            down_stack.pop_back();
        }
        if (!down_stack.empty()) {
            ans[i] = down_stack.back() + 1;
        }
        else {
            ans[i] = 0;
        }
        down_stack.push_back(i);
    }

    for (int i = 0; i < n; ++i) {
        printf("%d ", ans[i]);
    }

    return 0;
}

```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-21 141335.png"></img>


### 09202: 舰队、海域出击！

http://cs101.openjudge.cn/practice/09202/



思路：



代码

```python
# 
from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    degree=[0]*(n+1)
    for i in range(m):
        x,y=map(int,input().split())
        degree[y]+=1
        graph[x].append(y)
    q=deque()
    for i in range(1,n+1):
        if degree[i]==0:
            q.append(i)
    cnt=0
    while 1:
        if not q:
            print('Yes')
            break
        s=q.popleft()
        cnt+=1
        if cnt==n:
            print('No')
            break
        for nex in graph[s]:
            degree[nex]-=1
            if degree[nex]==0:
                q.append(nex)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-21 144838.png"></img>


### 04135: 月度开销

http://cs101.openjudge.cn/practice/04135/



思路：



代码

```python
# 
n,m=map(int,input().split())
arr=[int(input()) for i in range(n)]
def check(x):
    cnt=1
    tmp=0
    for i in range(n):
        if arr[i]>x:
            return 0
        if tmp+arr[i]>x:
            cnt+=1
            tmp=arr[i]
            if cnt>m:
                break
        else:
            tmp+=arr[i]
    return cnt<=m
l=1
r=sum(arr)
while 1:
    if l+1==r:
        if check(l):
            print(l)
            break
        print(r)
        break
    if l==r:
        print(l)
        break
    mid=(l+r)//2
    if check(mid):
        r=mid
    else:
        l=mid
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-21 150903.png"></img>


### 07735: 道路

http://cs101.openjudge.cn/practice/07735/



思路：



代码

```python
# 
import heapq
k=int(input())
n=int(input())
r=int(input())
graph=[[] for i in range(n+1)]
for i in range(r):
    s,d,l,t=map(int,input().split())
    graph[s].append((l,d,t))
q=[]
vis=set()
vis.add((1,0))
now=(0,1,0)
flag=0
while 1:
    l,d,t=now
    if now[1]==n:
        print(now[0])
        break
    for nex in graph[d]:
        if t+nex[2]<=k and not (nex[1],t+nex[2]) in vis:
            heapq.heappush(q,(l+nex[0],nex[1],t+nex[2]))
    while 1:
        if not q:
            flag=1
            break
        now=heapq.heappop(q)
        if not (now[1],now[2]) in vis:
            vis.add((now[1],now[2]))
            break
    if flag:
        print(-1)
        break
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-21 152731.png"></img>


### 01182: 食物链

http://cs101.openjudge.cn/practice/01182/



思路：



代码

```python
# 
n,k=map(int,input().split())
fa=[i for i in range(3*n+1)]
def get_fa(x):
    if fa[x]==x:
        return x
    fa[x]=get_fa(fa[x])
    return fa[x]
cnt=0
for _ in range(k):
    d,x,y=map(int,input().split())
    if x>n or y>n:
        cnt+=1
        continue
    if d==1:
        if get_fa(x)==get_fa(y+n) or get_fa(y)==get_fa(x+n):
            cnt+=1
        else:
            fa[get_fa(x)]=get_fa(y)
            fa[get_fa(x+n)]=get_fa(y+n)
            fa[get_fa(x+2*n)]=get_fa(y+2*n)
    else:
        if get_fa(x)==get_fa(y) or get_fa(y+n)==get_fa(x):
            cnt+=1
        else:
            fa[get_fa(x+n)]=get_fa(y)
            fa[get_fa(x+2*n)]=get_fa(y+n)
            fa[get_fa(x)]=get_fa(y+2*n)
print(cnt)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==


<img src="./代码截图/屏幕截图 2024-05-21 154309.png"></img>


## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

都是经典老题目，熟练掌握套路还是很简单的

现在的个人的重心是复习笔试内容



