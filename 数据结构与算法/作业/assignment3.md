# Assignment #3: March月考

Updated 1537 GMT+8 March 6, 2024

2024 spring, Complied by 陈涛 经济学院==同学的姓名、院系==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：vscode,python3.9

C/C++编程环境：vs2022



## 1. 题目

**02945: 拦截导弹**

http://cs101.openjudge.cn/practice/02945/



思路：



##### 代码

```python
# 
k=int(input())
arr=list(map(int,input().split()))
dp=[1]*k
for i in range(k):
    for j in range(i):
        if arr[i]<=arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))

```



代码运行截图 ==（至少包含有"Accepted"）==


<img src="./代码截图/屏幕截图 2024-03-06 193841.png"></img>


**04147:汉诺塔问题(Tower of Hanoi)**

http://cs101.openjudge.cn/practice/04147



思路：



##### 代码

```python
# 
def f(ori,temp,tar,n,max):
    if n==1:
        print(f'{max}:{ori}->{tar}')
        return
    f(ori,tar,temp,n-1,max-1)
    f(ori,temp,tar,1,max)
    f(temp,ori,tar,n-1,max-1)
n,a,b,c=input().split()
n=int(n)
f(a,b,c,n,n)
```



代码运行截图 ==（至少包含有"Accepted"）==


<img src="./代码截图/屏幕截图 2024-03-06 194856.png"></img>


**03253: 约瑟夫问题No.2**

http://cs101.openjudge.cn/practice/03253



思路：



##### 代码

```python
# 
class node:
    def __init__(self) -> None:
        self.num=None
        self.prev=None
        self.next=None
while 1:
    n,p,m=map(int,input().split())
    if n==0:
        break
    root=node()
    root.num=1
    now=root
    for i in range(2,n+1):
        now.next=node()
        now.next.num=i
        now.next.prev=now
        now=now.next
    now.next=root
    root.prev=now
    while 1:
        if now.num==p:
            break
        now=now.next
    cnt=0
    ans=[]
    while 1:
        if now.num==now.next.num:
            ans.append(str(now.num))
            break
        if cnt==m-1:
            now.prev.next=now.next
            now.next.prev=now.prev
            ans.append(str(now.num))
        cnt=(cnt+1)%m
        now=now.next
    print(','.join(ans))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-06 200112.png"></img>



**21554:排队做实验 (greedy)v0.2**

http://cs101.openjudge.cn/practice/21554



思路：



##### 代码

```python
# 
n=int(input())
arrs=list(map(int,input().split()))
arr=[(arrs[i],i+1) for i in range(n)]
arr.sort()
cnt=0
ans=0
for i in range(n):
    ans+=cnt
    cnt+=arr[i][0]
print(' '.join([str(arr[i][1]) for i in range(n)]))
print(f'{ans/n:.2f}')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-06 200847.png"></img>


**19963:买学区房**

http://cs101.openjudge.cn/practice/19963



思路：



##### 代码

```python
# 
n=int(input())
diss=input().split()
dis=[int(diss[i][1:-1].split(',')[0])+int(diss[i][1:-1].split(',')[1]) for i in range(n)]
price=list(map(int,input().split()))
able=[dis[i]/price[i] for i in range(n)]
oldp=price[:]
olda=able[:]
price.sort()
able.sort()
if n&1:
    mida=able[n//2]
    midp=price[n//2]
else:
    mida=(able[n//2]+able[n//2-1])/2
    midp=(price[n//2]+price[n//2-1])/2
ans=0
for i in range(n):
    if oldp[i]<midp and olda[i]>mida:
        ans+=1
print(ans)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-06 202201.png"></img>


**27300: 模型整理**

http://cs101.openjudge.cn/practice/27300



思路：



##### 代码

```python
# 
def cal(num):
    if num[-1]=='M':
        return float(num[:-1])
    else:
        return float(num[:-1])*1000
n=int(input())
d={}
name=[]
for i in range(n):
    s,num=input().split('-')
    try:
        d[s].append((cal(num),num))
    except:
        d[s]=[(cal(num),num)]
        name.append(s)
name.sort()
for i in name:
    d[i].sort()
    print(f'{i}: '+', '.join([k[1] for k in d[i]]))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-03-06 203017.png"></img>




## 2. 学习总结和收获

最近在做树相关的题目，感觉对栈和递归的理解加深了很多，现在虽然手上在写递归，但是其实心里想的是栈的实现方式

一直在用列表来实现树，暂时没感觉没有什么问题，而且挺方便

这次月考大概用了一个小时做完，写链表不是很熟练，比较慢

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==





