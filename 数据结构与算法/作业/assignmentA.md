# Assignment #A: 图论：算法，树算及栈

Updated 2018 GMT+8 Apr 21, 2024

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

### 20743: 整人的提词本

http://cs101.openjudge.cn/practice/20743/



思路：



代码

```c++
#include <iostream>
#include<vector>
using namespace std;

int main(){
	string s;
	cin >> s;
	vector<char> ans;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == ')') {
			vector<char> tmp;
			while (1) {
				if (ans.back() == '(') {
					ans.pop_back();
					break;
				}
				tmp.push_back(ans.back());
				ans.pop_back();
			}
			for (int i = 0; i < tmp.size(); i++) {
				ans.push_back(tmp[i]);
			}
			continue;
		}
		ans.push_back(s[i]);
	}
	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i];
	}
}
```



代码运行截图 ==（至少包含有"Accepted"）==


<img src="./代码截图/屏幕截图 2024-04-27 142201.png"></img>


### 02255: 重建二叉树

http://cs101.openjudge.cn/practice/02255/



思路：



代码

```python
# 
try:
    while 1:
        pre,mid=input().split()
        tree=[]
        index=0
        def f(mid,tree):
            global index
            if not mid:
                return
            tree.extend([pre[index],[],[]])
            sp=mid.index(pre[index])
            index+=1
            f(mid[0:sp],tree[1])
            f(mid[sp+1:],tree[2])
        f(mid,tree)
        ans=[]
        def g(tree):
            if not tree:
                return
            g(tree[1])
            g(tree[2])
            ans.append(tree[0])
        g(tree)
        print(''.join(ans))
except:
    pass
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-27 120431.png"></img>

### 01426: Find The Multiple

http://cs101.openjudge.cn/practice/01426/

要求用bfs实现



思路：



代码

```python
# 
from collections import deque
while 1:
    n=int(input())
    if n==0:
        break
    q=deque()
    now='1'
    while 1:
        if int(now)%n==0:
            print(now)
            break
        q.append(now+'1')
        q.append(now+'0')
        now=q.popleft()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-27 124922.png"></img>


### 04115: 鸣人和佐助

bfs, http://cs101.openjudge.cn/practice/04115/



思路：



代码

```python
# 
from collections import deque
dire=[(-1,0),(0,1),(1,0),(0,-1)]
m,n,t=map(int,input().split())
graph=[input() for _ in range(m)]
vis=[[[0]*(t+1) for _ in range(n)] for _ in range(m)]
q=deque()
for i in range(m):
    for j in range(n):
        if graph[i][j]=='@':
            now=(i,j,0,0)
            break
vis[now[0]][now[1]][0]=1
r=-1
while 1:
    if graph[now[0]][now[1]]=='+':
        r=now[3]
        break
    for dir in dire:
        if not(0<=now[0]+dir[0]<m and 0<=now[1]+dir[1]<n):
                continue
        if graph[now[0]+dir[0]][now[1]+dir[1]]!='#' and not vis[now[0]+dir[0]][now[1]+dir[1]][now[2]]:
            vis[now[0]+dir[0]][now[1]+dir[1]][now[2]]=1
            q.append((now[0]+dir[0],now[1]+dir[1],now[2],now[3]+1))
        elif now[2]+1<=t and not vis[now[0]+dir[0]][now[1]+dir[1]][now[2]+1]:
            vis[now[0]+dir[0]][now[1]+dir[1]][now[2]+1]=1
            q.append((now[0]+dir[0],now[1]+dir[1],now[2]+1,now[3]+1))
    if not q:
        break
    now = q.popleft()
print(r)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-27 132302.png"></img>


### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/



思路：



代码

```python
# 
import heapq
dire=[(-1,0),(0,-1),(1,0),(0,1)]
m,n,p=map(int,input().split())
graph=[input().split() for _ in range(m)]
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    if graph[x1][y1]=='#' or graph[x2][y2]=='#':
        print('NO')
        continue
    vis=[[0]*n for _ in range(m)]
    q=[]
    now=(0,x1,y1)
    vis[x1][y1]=1
    res='NO'
    while 1:
        if now[1]==x2 and now[2]==y2:
            res=now[0]
            break
        v = int(graph[now[1]][now[2]])
        for dir in dire:
            if not(0<=now[1]+dir[0]<m and 0<=now[2]+dir[1]<n):
                continue
            if vis[now[1]+dir[0]][now[2]+dir[1]] or graph[now[1]+dir[0]][now[2]+dir[1]]=='#':
                continue
            heapq.heappush(q,(now[0]+abs(int(graph[now[1]+dir[0]][now[2]+dir[1]])-v),now[1]+dir[0],now[2]+dir[1]))
        try:    
            while 1:
                now = heapq.heappop(q)
                if not vis[now[1]][now[2]]:
                    vis[now[1]][now[2]]=1
                    break
        except:
            break
    print(res)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-27 134428.png"></img>

### 05442: 兔子与星空

Prim, http://cs101.openjudge.cn/practice/05442/



思路：



代码

```python
# 
import heapq
n=int(input())
graph=[[] for _ in range(n)]
for _ in range(n-1):
    inp=input().split()
    node=ord(inp[0])-65
    m=int(inp[1])
    for k in range(m):
        graph[node].append((int(inp[2*k+3]),ord(inp[2*k+2])-65))
        graph[ord(inp[2*k+2])-65].append((int(inp[2*k+3]),node))

q=[]
vis=[0]*n
now=(0,0)
cnt=0
ans=0
vis[0]=1
while 1:
    ans+=now[0]
    if cnt==n-1:
        break
    for next in graph[now[1]]:
        if not vis[next[1]]:
            heapq.heappush(q,next)
    while 1:
        now=heapq.heappop(q)
        if not vis[now[1]]:
            vis[now[1]]=1
            break
    cnt+=1
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-27 141041.png"></img>


## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==


作业题都是很经典的题目, 重新做了一遍再复习了一下各种图算法

学ai的时候学会了两个深搜的启发原则：选择下一个待赋值变量的时候优先选择限制最多的; 给变量的赋值选择能让待赋值变量限制最少的