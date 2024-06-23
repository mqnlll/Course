# Assignment #8: 图论：概念、遍历，及 树算

Updated 1919 GMT+8 Apr 8, 2024

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

### 19943: 图的拉普拉斯矩阵

matrices, http://cs101.openjudge.cn/practice/19943/

请定义Vertex类，Graph类，然后实现



思路：



代码

```python
# 
n,m=map(int,input().split())
d=[0 for _ in range(n)]
a=[[0]*n for _ in range(n)]
for _ in range(m):
    x,y=map(int,input().split())
    d[x]+=1
    d[y]+=1
    a[x][y]=a[y][x]=-1
for i in range(n):
    a[i][i]+=d[i]
for i in range(n):
    print(' '.join(map(str,a[i])))
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-10 211459.png"></img>



### 18160: 最大连通域面积

matrix/dfs similar, http://cs101.openjudge.cn/practice/18160



思路：



代码

```python
# 
t=int(input())
dire=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[0]*n
    for i in range(n):
        matrix[i]=input()
    vis=[[0]*m for i in range(n)]
    cnt=0
    def dfs(x,y):
        global cnt
        if x<0 or x>=n or y<0 or y>=m:
            return
        if vis[x][y]:
            return
        if matrix[x][y]=='.':
            return
        vis[x][y]=1
        cnt+=1
        for dir in dire:
            dfs(x+dir[0],y+dir[1])
    ans=0
    for x in range(n):
        for y in range(m):
            cnt=0
            dfs(x,y)
            ans=max(ans,cnt)
    print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-10 205815.png"></img>


### sy383: 最大权值连通块

https://sunnywhy.com/sfbj/10/3/383



思路：



代码

```python
# 
n,m=map(int,input().split())
value=list(map(int,input().split()))
g=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
vis=[0]*n
cnt=0
def dfs(x):
    global cnt
    if vis[x]:
        return
    cnt+=value[x]
    vis[x]=1
    for i in g[x]:
        dfs(i)
ans=0
for i in range(n):
    cnt=0
    dfs(i)
    ans=max(ans,cnt)
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-10 204353.png"></img>


### 03441: 4 Values whose Sum is 0

data structure/binary search, http://cs101.openjudge.cn/practice/03441



思路：



代码

```c++
#include <iostream>
#include<unordered_map>
using namespace std;


int m12[4001][4001];
int m[4][4001];
unordered_map<int, int> m34;

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		scanf("%d", &m[0][i]); scanf("%d", &m[1][i]); scanf("%d", &m[2][i]); scanf("%d", &m[3][i]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			m12[i][j] = m[0][i] + m[1][j];
			if (m34.count(m[2][i] + m[3][j])) {
				m34[m[2][i] + m[3][j]] += 1;
			}
			else {
				m34[m[2][i] + m[3][j]] = 1;
			}
		}
	}
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (m34.count(-m12[i][j])) {
				cnt += m34[-m12[i][j]];
			}
		}
	}
	cout << cnt << endl;
}

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-10 211759.png"></img>

### 04089: 电话号码

trie, http://cs101.openjudge.cn/practice/04089/

Trie 数据结构可能需要自学下。



思路：



代码

```python
# 
class node:
    def __init__(self,val=-1) -> None:
        self.val=val
        self.isend=0
        self.children=[None]*10

t=int(input())
for _ in range(t):
    n=int(input())
    flag=1
    root=node()
    for k in range(n):
        s=input()
        now=root
        if not flag:
            continue
        for i in range(len(s)):
            if i==len(s)-1 and now.children[int(s[i])]:
                flag=0
                break
            if not now.children[int(s[i])]:
                now.children[int(s[i])]=node(int(s[i]))
            now=now.children[int(s[i])]
            if now.isend:
                flag=0
                break
        now.isend=1
    print('YES' if flag else 'NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-10 211941.png"></img>


### 04082: 树的镜面映射

http://cs101.openjudge.cn/practice/04082/



思路：



代码

```python
# 
tree=[]
i=0
n=int(input())
pre=input().split()
def f(tree):
    global i
    node,flag=pre[i][0],pre[i][1]
    if node=='$':
        return
    tree.append([node,[]])
    if flag=='0':
        i+=1
        f(tree[-1][1])
        i+=1
        f(tree)
f(tree)

from collections import deque
q=deque()
q.append(tree[0])
ans=[]
cnt=0
while len(q)>0:
    now=q.popleft()
    if not now:
        continue
    ans.append(now[0])
    for i in range(len(now[1])):
        q.append(now[1][len(now[1])-i-1])
print(' '.join(ans))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-04-10 195738.png"></img>

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==





