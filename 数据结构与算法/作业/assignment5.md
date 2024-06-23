# Assignment #5: "树"算：概念、表示、解析、遍历

Updated 2124 GMT+8 March 17, 2024

2024 spring, Complied by 陈涛 经济学院==同学的姓名、院系==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:

Learn about Time complexities, learn the basics of individual Data Structures, learn the basics of Algorithms, and practice Problems.

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：vscode,python3.10

C/C++编程环境：vs2022



## 1. 题目

### 27638: 求二叉树的高度和叶子数目

http://cs101.openjudge.cn/practice/27638/



思路：



代码

```python
# 
n=int(input())
nodes=[0]*n
nums=0
for i in range(n):
    nodes[i]=tuple(map(int,input().split()))
    if nodes[i][0]==-1 and nodes[i][1]==-1:
        nums+=1
height=0
vis=[0]*n
def dfs(node,depth):
    global height
    if vis[node]:
        return
    vis[node]=1
    if nodes[node][0]!=-1:
        dfs(nodes[node][0],depth+1)
    if nodes[node][1]!=-1:
        dfs(nodes[node][1],depth+1)
    height=max(height,depth)
    vis[node]=0
for i in range(n):
    dfs(i,0)
print(height,nums)
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-18 112924.png"></img>

### 24729: 括号嵌套树

http://cs101.openjudge.cn/practice/24729/



思路：



代码

```python
# 
n=int(input())
tree=[]
ans=''
index=0
def bulid(s,tree):
    global index
    tree.append(s[index])
    index+=1
    tree.append([])
    tree.append([])
    try:
        if s[index]=='(':
            index+=1
            bulid(s,tree[1])
            if s[index]==',':
                index+=1
                bulid(s,tree[2])
            index+=1
        else:
            return
    except:
        pass
def pre(tree):
    if len(tree)==0 or tree[0]=='*':
        return
    global ans
    ans+=tree[0]
    pre(tree[1])
    pre(tree[2])
def mid(tree):
    if len(tree)==0 or tree[0]=='*':
        return
    global ans
    mid(tree[1])
    ans+=tree[0]
    mid(tree[2])
while n>0:
    n-=1
    s=input()
    index=0
    tree=[]
    bulid(s,tree)
    ans=''
    pre(tree)
    print(ans)
    ans=''
    mid(tree)
    print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-18 113542.png"></img>

### 02775: 文件结构“图”

http://cs101.openjudge.cn/practice/02775/



思路：



代码

```python
# 
cnt=0
while 1:
    cnt+=1
    root=['ROOT',[],[]]
    ss=[]
    while 1:
        s=input()
        if s=='#':
            break
        if s=='*':
            break
        ss.append(s)
    if not ss:
        break
    index=0
    def f(root):
        global index
        while 1:
            if index==len(ss):
                return
            if ss[index][0]=='d':
                root[1].append([ss[index],[],[]])
                index+=1
                f(root[1][-1])
            elif ss[index][0]=='f':
                root[2].append(ss[index])
                index+=1
            else:
                index+=1
                return
    f(root)
    print(f'DATA SET {cnt}:')
    def g(root,depth):
        print('|     '*depth+root[0])
        for dir in root[1]:
            g(dir,depth+1)
        root[2].sort()
        for file in root[2]:
            print('|     '*depth+file)
    g(root,0)
    print()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-18 120440.png"></img>


### 25140: 根据后序表达式建立队列表达式

http://cs101.openjudge.cn/practice/25140/



思路：



代码

```python
# 
import queue
i=0
def f(tree:list,s:str):
    global i
    tree.extend([0,[],[]])
    tree[0]=s[i]
    i-=1
    if s[i+1].islower():
        return
    f(tree[2],s)
    f(tree[1],s)
def g(tree):
    ans=[]
    q=queue.Queue()
    q.put(tree)
    while not q.empty():
        now=q.get()
        if now:
            ans.append(now[0])
            q.put(now[1])
            q.put(now[2])
    return ''.join(ans)[::-1]
n=int(input())
for _ in range(n):
    s=input()
    i=len(s)-1
    tree=[]
    f(tree,s)
    print(g(tree))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-18 163203.png"></img>

### 24750: 根据二叉树中后序序列建树

http://cs101.openjudge.cn/practice/24750/



思路：



代码

```python
# 
r=0
def f(tree:list,s1:str,s2):
    if not s1:
        return
    global r
    r-=1
    tree.extend([0,[],[]])
    tree[0]=s2[r]
    if len(s1)==1:
        return
    f(tree[2],s1[s1.find(tree[0])+1:],s2)
    f(tree[1],s1[:s1.find(tree[0])],s2)
ans=[]
def g(tree:list):
    if not tree:
        return
    ans.append(tree[0])
    g(tree[1])
    g(tree[2])
s1,s2=input(),input()
r=len(s2)
tree=[]
f(tree,s1,s2)
g(tree)
print(''.join(ans))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-18 163500.png"></img>


### 22158: 根据二叉树前中序序列建树

http://cs101.openjudge.cn/practice/22158/



思路：



代码

```python
# 
try:
    while 1:
        suf=''
        pre,mid=input(),input()
        i=-1
        def f(mid):
            global i,suf
            if(len(mid)==0):
                return
            i+=1
            if(len(mid)==1):
                suf+=pre[i]
                return
            tmp=pre[i]
            index=mid.find(tmp)
            left=mid[0:index]
            right=mid[index+1:]
            f(left)
            f(right)
            suf+=tmp
        f(mid)
        print(suf)
except EOFError:
    pass
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-18 164509.png"></img>



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

基本把数算pre中的树的题目做完了

学了二叉搜索树和avl

学了堆的二叉树实现



