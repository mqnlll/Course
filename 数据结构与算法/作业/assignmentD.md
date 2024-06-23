# Assignment #D: May月考

Updated 1654 GMT+8 May 8, 2024

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

### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：



代码

```python
# 
l,m=map(int,input().split())
arr=[0]*(l+1)
for _ in range(m):
    s,e=map(int,input().split())
    arr[s]+=1
    arr[e]-=1
pre_sum = [0]*(l+1)
pre_sum[0]=arr[0]
for i in range(1,l+1):
    pre_sum[i] = pre_sum[i-1] + arr[i]
ans=0
for i in range(l+1):
    if not arr[i] and not pre_sum[i]:
        ans+=1
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-12 143739.png"></img>


### 20449: 是否被5整除

http://cs101.openjudge.cn/practice/20449/



思路：



代码

```python
# 
s=input()
ans=''
for i in range(1,len(s)+1):
    if int(s[0:i],2)%5==0:
        ans+='1'
    else:
        ans+='0'
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-12 144303.png"></img>

### 01258: Agri-Net

http://cs101.openjudge.cn/practice/01258/



思路：



代码

```python
# 
import heapq
try:
    while 1:
        n=int(input())
        graph=[[] for _ in range(n)]
        for i in range(n):
            inp=list(map(int,input().split()))
            for k in range(n):
                graph[i].append((inp[k],k))
        q=[]
        vis=[0]*n
        now = (0,0)
        vis[0]=1
        cnt=0
        ans=0
        while 1:
            for nex in graph[now[1]]:
                if not vis[nex[1]]:
                    heapq.heappush(q,nex)
            while 1:
                now = heapq.heappop(q)
                if not vis[now[1]]:
                    vis[now[1]]=1
                    cnt+=1
                    ans+=now[0]
                    break
            if cnt==n-1:
                break
        print(ans)
except:
    pass          
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-12 145413.png"></img>



### 27635: 判断无向图是否连通有无回路(同23163)

http://cs101.openjudge.cn/practice/27635/



思路：



代码

```python
# 
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
def check_con():
    vis=[0]*n
    def dfs1(x):
        if vis[x]:
            return
        vis[x]=1
        for nex in graph[x]:
            dfs1(nex)
    dfs1(0)
    return all(vis)
def check_loop():
    vis=[0]*n
    flag=0
    def dfs2(x,fa):
        nonlocal flag
        if flag:
            return
        if vis[x]:
            flag=1
            return
        vis[x]=1
        for nex in graph[x]:
            if nex!=fa:
                dfs2(nex,x)
    for i in range(n):
        if not vis[i]:
            dfs2(i,-1)
    return flag
if check_con():
    print('connected:yes')
else:
    print('connected:no')
if check_loop():
    print('loop:yes')
else:
    print('loop:no')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-12 151426.png"></img>



### 27947: 动态中位数

http://cs101.openjudge.cn/practice/27947/



思路：



代码

```python
# 
import heapq
t=int(input())
for _ in range(t):
    arr=list(map(int,input().split()))
    less=[] #大根
    great=[] #小根
    les_num=0
    great_num=1
    ans=[]
    ans.append(str(arr[0]))
    great.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]<great[0]:
            heapq.heappush(less,-arr[i])
            les_num +=1
        else:
            heapq.heappush(great,arr[i])
            great_num +=1
        if great_num > les_num + 1:
            heapq.heappush(less,-heapq.heappop(great))
            les_num += 1
            great_num -= 1
        if les_num > great_num:
            heapq.heappush(great,-heapq.heappop(less))
            les_num -= 1
            great_num += 1
        if i%2==0:
            ans.append(str(great[0]))
    print(len(ans))
    print(' '.join(ans))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-12 153657.png"></img>


### 28190: 奶牛排队

http://cs101.openjudge.cn/practice/28190/



思路：



代码

```python
# 
import bisect
n=int(input())
arr=[int(input()) for _ in range(n)]
up_stack=[]
down_stack=[]
ans=0
for i in range(n):
    while up_stack and arr[up_stack[-1]]>=arr[i]:
        up_stack.pop()
    while down_stack and arr[down_stack[-1]]<arr[i]:
        down_stack.pop()
    if down_stack:
        tmp=bisect.bisect_right(up_stack,down_stack[-1])
    else:
        tmp=bisect.bisect_right(up_stack,-1)
    if tmp!=len(up_stack):
        ans=max(ans,i-up_stack[tmp]+1)
    up_stack.append(i)
    down_stack.append(i)
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-05-12 231039.png"></img>



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

之前对单调栈的认识只停留在 最大矩形面积 那道题目，这次真是狠狠加深了对单调栈的理解

之前只会维护[0:i]的最值，而单调栈能维护[0:i]中所有可能的最值的分布

                                                                                                                                    