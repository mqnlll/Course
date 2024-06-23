# Assignment #6: "树"算：Huffman,BinHeap,BST,AVL,DisjointSet

Updated 2214 GMT+8 March 24, 2024

2024 spring, Complied by 陈涛 经济学院==同学的姓名、院系==



**说明：**

1）这次作业内容不简单，耗时长的话直接参考题解。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：vscode,python3.10

C/C++编程环境：vs2022



## 1. 题目

### 22275: 二叉搜索树的遍历

http://cs101.openjudge.cn/practice/22275/



思路：



代码

```python
# 
import sys
sys.setrecursionlimit(1<<30)
n=int(input())
pre=list(map(int,input().split()))
def f(l,r):
    if l==r:
        return []
    tree=[pre[l],[],[]]
    if l+1==r:
        return tree
    flag=0
    for i in range(l+1,r):
        if pre[i]>pre[l]:
            tree[1]=f(l+1,i)
            tree[2]=f(i,r)
            flag=1
            break
    if not flag:
        tree[1]=f(l+1,r)
    return tree
tree=f(0,n)
ans=[]
def g(tree):
    if not tree:
        return
    g(tree[1])
    g(tree[2])
    ans.append(str(tree[0]))
g(tree)
print(' '.join(ans))
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-25 134637.png"></img>

### 05455: 二叉搜索树的层次遍历

http://cs101.openjudge.cn/practice/05455/



思路：



代码

```python
# 
import queue
class node:
    def __init__(self,n=None) -> None:
        self.num=n
        self.left:node=None
        self.right:node=None
def insert(root,x):
    if not root:
        return node(x)
    if x>root.num:
        root.right=insert(root.right,x)
    else:
        root.left=insert(root.left,x)
    return root
s=list(map(int,input().split()))
vis=set()
root=node()
for x in s:
    if x in vis:
        continue
    vis.add(x)
    if not root.num:
        root.num=x
        continue
    insert(root,x)
q=queue.Queue()
q.put(root)
ans=[]
while not q.empty():
    now=q.get()
    if now:
        ans.append(str(now.num))
        q.put(now.left)
        q.put(now.right)
print(' '.join(ans))
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-25 134945.png"></img>


### 04078: 实现堆结构

http://cs101.openjudge.cn/practice/04078/

练习自己写个BinHeap。当然机考时候，如果遇到这样题目，直接import heapq。手搓栈、队列、堆、AVL等，考试前需要搓个遍。



思路：



代码

```python
# 
class heap:
    def __init__(self) -> None:
        self.arr=[]
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def put(self,n):
        self.arr.append(n)
        i=len(self.arr)-1
        while i!=0 and self.arr[self.parent(i)]>n:
            self.arr[self.parent(i)],self.arr[i]=self.arr[i],self.arr[self.parent(i)]
            i=self.parent(i)

    def get(self):
        smallest=self.arr[0]
        self.arr[0]=self.arr[-1]
        self.arr.pop()
        self.heapify(0)
        return smallest
        
    def heapify(self,i):
        smallest=i
        l=self.left(i)
        r=self.right(i)
        if l<len(self.arr) and self.arr[smallest]>self.arr[l]:
            smallest=l
        if r<len(self.arr) and self.arr[smallest]>self.arr[r]:
            smallest=r
        if smallest!=i:
            self.arr[smallest],self.arr[i]=self.arr[i],self.arr[smallest]
            self.heapify(smallest)
    
q=heap()
n=int(input())
for _ in range(n):
    s=input().split()
    if s[0]=='1':
        q.put(int(s[1]))
    else:
        print(q.get())
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-25 144204.png"></img>


### 22161: 哈夫曼编码树

http://cs101.openjudge.cn/practice/22161/



思路：



代码

```python
# 
import heapq
q=[]
n=int(input())
for _ in range(n):
    c,num=input().split()
    heapq.heappush(q,(int(num),[c,[],[]]))
while 1:
    if len(q)==1:
        break
    l_num,l_c=heapq.heappop(q)
    r_num,r_c=heapq.heappop(q)
    if l_num==r_num and l_c[0][0]>r_c[0][0]:
        l_c,r_c=r_c,l_c
    new=[''.join(sorted(l_c[0]+r_c[0])),l_c,r_c]
    heapq.heappush(q,(l_num+r_num,new))
tree=q[0][1]
code_c={}
c_code={}
def code(tree,cod):
    if len(tree[0])==1:
        c_code[tree[0]]=cod
        code_c[cod]=tree[0]
        return
    code(tree[1],cod+'0')
    code(tree[2],cod+'1')
code(tree,'')
try:
    while 1:
        s=input()
        if s[0] in c_code:
            ans=''
            for c in s:
                ans+=c_code[c]
            print(ans)
        else:
            ans=''
            l=0
            for r in range(1,len(s)+1):
                if s[l:r] in code_c:
                    ans+=code_c[s[l:r]]
                    l=r
            print(ans)
except:
    pass
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-25 152950.png"></img>


### 晴问9.5: 平衡二叉树的建立

https://sunnywhy.com/sfbj/9/5/359



思路：



代码

```python
# 
class Node:
    def __init__(self,n=None) -> None:
        self.num=n
        self.left=None
        self.right=None
        self.height=1
class AVL:
    def get_height(self,root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self,root):
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)

    def left_rotate(self,z:Node):
        y=z.right
        t2=y.left
        y.left=z
        z.right=t2
        
        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))

        return y

    def right_rotate(self,y:Node):
        x=y.left
        t2=x.right
        x.right=y
        y.left=t2

        y.height=1+max(self.get_height(y.left),self.get_height(y.right))
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))

        return x

    def insert(self,root,n):
        if not root:
            return Node(n)
        if n<root.num:
            root.left=self.insert(root.left,n)
        else:
            root.right=self.insert(root.right,n)

        root.height=1+max(self.get_height(root.left),self.get_height(root.right))

        balance=self.get_balance(root)

        if balance>1 and n<root.left.num:
            root=self.right_rotate(root)
        elif balance<-1 and n>root.right.num:
            root=self.left_rotate(root)
        elif balance>1 and n>root.left.num:
            root.left=self.left_rotate(root.left)
            root=self.right_rotate(root)
        elif balance<-1 and n<root.right.num:
            root.right=self.right_rotate(root.right)
            root=self.left_rotate(root)

        return root

    def pre(self,root,ans):
        if not root:
            return
        ans.append(str(root.num))
        self.pre(root.left,ans)
        self.pre(root.right,ans)
        return ans
n=int(input())
arr=list(map(int,input().split()))
root=Node(arr[0])
avl=AVL()
for i in range(1,n):
    root=avl.insert(root,arr[i])
ans=avl.pre(root,[])
print(' '.join(ans))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-25 204747.png"></img>


### 02524: 宗教信仰

http://cs101.openjudge.cn/practice/02524/



思路：



代码

```python
# 
ca=1
while 1:
    n,m=map(int,input().split())
    if n==0:
        break
    fa=[i for i in range(n+1)]
    def get_fa(i):
        if fa[i]==i:
            return i
        fa[i]=get_fa(fa[i])
        return fa[i]
    for _ in range(m):
        a,b=map(int,input().split())
        fa[get_fa(a)]=get_fa(b)
    cnt=0
    for i in range(1,n+1):
        if fa[i]==i:
            cnt+=1
    print(f'Case {ca}: {cnt}')
    ca+=1
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
<img src="./代码截图/屏幕截图 2024-03-25 155850.png"></img>





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

又手搓了一遍堆和avl，应该能彻底记住了

并查集的题目第一次做就是oj1182食物链，难度应该是比较高的




