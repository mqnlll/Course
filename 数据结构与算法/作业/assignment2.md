# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by 陈涛 经济学院==同学的姓名、院系==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 11

Python编程环境：vscode,python3.9

C/C++编程环境：vs2022



## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/2024sp_routine/27653/



思路：



##### 代码

```python
# 
from math import gcd
a,b,c,d=map(int,input().split())
t=b*d//gcd(b,d)
u=a*(t//b)+c*(t//d)
print(f'{u}/{t}')
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="代码截图/屏幕截图 2024-02-28 114010.png">



### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：



##### 代码

```c++
#include <stdio.h>
#include <stdlib.h>
#include<algorithm>
using namespace std;

struct candy
{
	int w; int v;
	float p;
	candy(float tw,float tv) {
		w = tw;
		v = tv;
		p = tv / tw;
	}
	candy() {};
};

bool cmp(candy a, candy b) {
	return a.p > b.p;
}

int main() {
	candy cans[100];
	int n,w;
	scanf("%d", &n); scanf("%d", &w);
	for (int i = 0; i < n; i++) {
		int tv, tw;
		scanf("%d", &tv); scanf("%d", &tw);
		cans[i] = candy(tw, tv);
	}
	sort(cans, cans + n, cmp);
	float ans = 0;
	int i = 0;
	while (i<n) {
		if (cans[i].w >= w) {
			ans += float(w) * cans[i].p;
			break;
		}
		ans += cans[i].v;
		w -= cans[i].w;
		i += 1;
	}
	printf("%.1f", ans);
}
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="代码截图/屏幕截图 2024-02-28 114149.png">



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：



##### 代码

```python
# 
ns=int(input())
while ns>0:
    ns-=1
    n,m,b=map(int,input().split())
    skills={}
    for i in range(n):
        t,x=map(int,input().split())
        try:
            skills[t].append(x)
        except:
            skills[t]=[x]
    for t in sorted(skills):
        skills[t].sort(reverse=True)
        for i in range(m):
            try:
                b-=skills[t][i]
            except:
                break
        if b<=0:
            print(t)
            break
    else:
        print('alive')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="代码截图/屏幕截图 2024-02-28 114256.png">



### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：



##### 代码

```c++
#include <stdio.h>
#include <stdlib.h>
#include<cstring>
#include<cmath>
using namespace std;
 
int not_p[10000001];
int main() {
	memset(not_p, 0, sizeof(not_p));
	not_p[0] = 1;
	not_p[1] = 1;
	for (int i = 2; i <= 1000000; i++) {
		if (!not_p[i]) {
			for (int k = 2 * i; k <= 1000000; k += i) {
				not_p[k] = 1;
			}
		}
	}
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		long long int t;
		scanf("%I64d", &t);
		double sq=sqrt(t);
		if (abs(round(sq)-sq)<0.000001 && !not_p[int(round(sq))]) {
			printf("%s \n", "YES");
		}
		else {
			printf("%s \n", "NO");
		}
	}
}

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
<img src="./代码截图/屏幕截图 2024-02-28 114456.png">




### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：



##### 代码

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include<cstring>
using namespace std;

int main() {
	int arr[100001];
	int t;
	scanf("%d", &t);
	while (t > 0) {
		--t;
		int arr[100001], n,x;
		scanf("%d", &n);
		scanf("%d", &x);
		int sum=0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &arr[i]);
			sum += arr[i];
		}
		if (sum % x != 0) {
			printf("%d \n", n);
			continue;
		}
		int l = 0, r = n - 1;
		while (l<=n-1) {
			if (arr[l] % x != 0) {
				break;
			}
			l++;
		}
		while (r >= 0) {
			if (arr[r] % x != 0) {
				break;
			}
			r--;
		}
		if (l > r) {
			printf("%d \n", -1);
		}
		else {
			printf("%d \n", n - l - 1 > r ? n - 1 - l : r);
		}
	}
}

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-02-28 114557.png">



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：



##### 代码

```python
# 
m,n=map(int,input().split())
arr=[1]*(10001)
l=10000
for i in range(2,l+1):
    if arr[i]==1:
        for k in range(2*i,l+1,i):
            arr[k]=0
for _ in range(m):
    scores=list(map(int,input().split()))
    Sum=0
    for i in scores:
        sqrt=i**(1/2)
        if sqrt==int(sqrt):
            if arr[int(sqrt)]:
                Sum+=i
    if Sum==0:
        print(0)
    else:
        print(f'{Sum/len(scores):.2f}')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="./代码截图/屏幕截图 2024-02-28 114650.png">



## 2. 学习总结和收获

在刷寒假选做里的题目，学习树和图相关的算法。基本掌握prim和迪杰斯特拉。

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==





