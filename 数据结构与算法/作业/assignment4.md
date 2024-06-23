# Assignment #4: 排序、栈、队列和树

Updated 0005 GMT+8 March 11, 2024

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

Python编程环境：vscode,python3.9

C/C++编程环境：vs2022



## 1. 题目

### 05902: 双端队列

http://cs101.openjudge.cn/practice/05902/



思路：



代码

```python
# 
t=int(input())
for i in range(t):
    n=int(input())
    q=[]
    l=0
    r=0
    for _ in range(n):
        ty,x=map(int,input().split())
        if ty==1:
            q.append(x)
            r+=1
        else:
            try:
                if x:
                    q.pop()
                    r-=1
                else:
                    l+=1
            except:
                pass
    if l<r:
        print(' '.join([str(q[i]) for i in range(l,r)]))
    else:
        print('NULL')
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-11 204739.png"></img>

### 02694: 波兰表达式

http://cs101.openjudge.cn/practice/02694/



思路：



代码

```python
# 
s=input().split()
stack=[]
while s:
    t=s.pop()
    if t in ['*','+','-','/']:
        l1,l2=stack.pop(),stack.pop()
        stack.append(eval(str(l1)+t+str(l2)))
    else:
        stack.append(t)
print(f'{stack[0]:.6f}')
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-11 205850.png"></img>


### 24591: 中序表达式转后序表达式

http://cs101.openjudge.cn/practice/24591/



思路：



代码

```python
# 
order={'(':0,'+':1,'-':1,'*':2,'/':2,')':3}
n=int(input())
for _ in range(n):
    s=input()
    ope=[]
    val=[]
    i=0
    while i<len(s):
        tmp=s[i]
        i+=1
        if not tmp in order:
            while i<len(s):
                if s[i] in order:
                    break
                tmp+=s[i]
                i+=1
            val.append(tmp)
            continue
        if tmp==')':
            while 1:
                if ope[-1]=='(':
                    ope.pop()
                    break
                val.append(ope.pop())
        elif tmp=='(':
            ope.append('(')
        else:
            while 1:
                if len(ope)==0 or order[ope[-1]]<order[tmp]:
                    ope.append(tmp)
                    break
                val.append(ope.pop())
    while ope:
        val.append(ope.pop())
    print(' '.join(val))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-11 213326.png"></img>


### 22068: 合法出栈序列

http://cs101.openjudge.cn/practice/22068/



思路：



代码

```python
# 
x=input()
try:
    while 1:
        s=input()
        if len(s)!=len(x):
            print("NO")
            continue
        stack=[]
        i=0
        i2=0
        flag=0
        while 1:
            if not stack:
                if i2==len(x):
                    break
                stack.append(x[i2])
                i2+=1
                continue
            if not stack[-1]==s[i]:
                if i2==len(x):
                    break
                stack.append(x[i2])
                i2+=1
                continue
            stack.pop()
            i+=1
            if i==len(s):
                print('YES')
                flag=1
                break
        if not flag:
            print('NO')
except:
    pass
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==


<img src="./代码截图/屏幕截图 2024-03-11 215300.png"></img>

### 06646: 二叉树的深度

http://cs101.openjudge.cn/practice/06646/



思路：



代码

```python
# 
n=int(input())
tree=[0]*(n+1)
for i in range(1,n+1):
    tree[i]=tuple(map(int,input().split()))
stack=[(1,0)]
ans=0
while stack:
    now,depth=stack.pop()
    if now==-1:
        ans=max(ans,depth)
        continue
    stack.append((tree[now][0],depth+1))
    stack.append((tree[now][1],depth+1))
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-11 220458.png"></img>


### 02299: Ultra-QuickSort

http://cs101.openjudge.cn/practice/02299/



思路：



代码

```python
# 
cnt=0
def f(arr,temp,l,r):
    if l+1==r:
        return
    global cnt
    l1=l
    r1=l2=((r-l)>>1)+l
    r2=r
    f(arr,temp,l1,r1)
    f(arr,temp,l2,r2)
    i,j,k=l1,l2,l
    while i<r1 and j<r2:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            i+=1
        else:
            temp[k]=arr[j]
            j+=1
            cnt+=r1-i
        k+=1
    while i<r1:
        temp[k]=arr[i]
        k+=1
        i+=1
    while j<r2:
        temp[k]=arr[j]
        k+=1
        j+=1
    for k in range(l,r):
        arr[k]=temp[k]
while 1:
    n=int(input())
    if n==0:
        break
    arr=[int(input()) for _ in range(n)]
    cnt=0
    f(arr,[0]*n,0,n)
    print(cnt)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-11 220612.png"></img>



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

已经熟练写链表

能用栈实现dfs

还在继续练习树的题目




