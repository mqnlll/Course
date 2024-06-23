# Assignment #7: April 月考

Updated 1557 GMT+8 Apr 3, 2024

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

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/



思路：



代码

```python
# 
s=input().split()
s.reverse()
print(' '.join(s))
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-06 170841.png"></img>


### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/



思路：



代码

```python
# 
import queue
q=queue.Queue()
num=0
m,n=map(int,input().split())
arr=input().split()
ans=0
vis=set()
for i in arr:
    if i in vis:
        continue
    ans+=1
    if num<m:
        q.put(i)
        vis.add(i)
        num+=1
    else:
        vis.remove(q.get())
        q.put(i)
        vis.add(i)
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-06 171102.png"></img>


### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/



思路：



代码

```python
# 
n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
if k==0:
    if arr[0]!=1:
        print(1)
    else:
        print(-1)
elif k>=n or arr[k]!=arr[k-1]:
    print(arr[k-1])
else:
    print(-1)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-06 171230.png"></img>


### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/



思路：



代码

```python
# 
t=[]
n=int(input())
s=input()
def f(s,tree):
    if '1' in s and '0' in s:
        r='F'
    elif '1' in s:
        r='I'
    else:
        r='B'
    tree.extend([r,[],[]])
    if len(s)==1:
        return
    f(s[0:len(s)//2],tree[1])
    f(s[len(s)//2:len(s)],tree[2])
f(s,t)
ans=[]
def g(tree):
    if not tree:
        return
    g(tree[1])
    g(tree[2])
    ans.append(tree[0])
g(t)
print(''.join(ans))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==


<img src="./代码截图/屏幕截图 2024-04-06 171402.png"></img>

### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/



思路：



代码

```python
# 
from collections import deque
t=int(input())
q_team=deque()
q_per=[deque() for _ in range(t)]
teams={}
for i in range(t):
    arr=list(input().split())
    for j in range(len(arr)):
        teams[arr[j]]=i
while 1:
    s=input().split()
    if s[0]=='STOP':
        break
    if s[0]=='DEQUEUE':
        x=q_per[q_team[0]].popleft()
        print(x)
        if len(q_per[q_team[0]])==0:
            q_team.popleft()
    else:
        x=s[1]
        if len(q_per[teams[x]])==0:
            q_team.append(teams[x])
        q_per[teams[x]].append(x)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-06 171520.png"></img>


### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/



思路：



代码

```python
# 
n=int(input())
nodes={}
not_root=set()
for _ in range(n):
    arr=list(map(int,input().split()))
    nodes[arr[0]]=arr[1:len(arr)]
    for i in range(1,len(arr)):
        not_root.add(arr[i])
for i in nodes.keys():
    if not i in not_root:
        root=i
def f(node):
    if not node in nodes:
        print(node)
        return
    order=[node]+nodes[node]
    order.sort()
    for v in order:
        if v==node:
            print(v)
            continue
        f(v)
f(root)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-06 171620.png"></img>



## 2. 学习总结和收获


后面两题读完题目没怎么想就直接去实现了，所以考试的时候写的代码都比较蠢，效率低而且写得还复杂

做完仔细想想更好的思路还是很显然的，考试时还是不能着急

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==





