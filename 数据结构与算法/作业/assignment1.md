# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2023 fall, Complied by 陈涛 经济学院==同学的姓名、院系==



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

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

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：



##### 代码

```c++

#include <iostream>
using namespace ::std;


int main() {
	int n;
	cin >> n;
	int t[31];
	t[0] = 0; t[1] = 1; t[2] = 1;
	for (int i = 3; i <= n; i++) {
		t[i] = t[i - 1] + t[i - 2] + t[i - 3];
	}
	cout << t[n];
}
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="代码截图/屏幕截图 2024-02-19 213231.png" >



### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：



##### 代码

```c++

#include <iostream>
using namespace ::std;
 
 
int main() {
	string s;
	cin >> s;
	char ss[] = "hello";
	int flag = 0;
	int index = 0;
	for (int i = 0; i < s.length(); i++) {
		if (index == 5)break;
		if (s[i] == ss[index]) {
			index++;
		}
	}
	if (index == 5) {
		cout << "YES";
	}
	else {
		cout << "NO";
	}
} 
```



代码运行截图 ==（至少包含有"Accepted"）==

<img src="代码截图/屏幕截图 2024-02-19 213320.png">



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：



##### 代码

```python
# 
vowel=['a','o','y','e','u','i']
s=input()
s=s.lower()
for i in s:
    if i in vowel:
        continue
    else:
        print('.'+i,end='')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
<img src="代码截图/屏幕截图 2024-02-19 214109.png" >




### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：



##### 代码

```c++
#include <iostream>
#include<cstring>
using namespace ::std;

int not_primes[10001];

int main() {
	memset(not_primes, 0, sizeof(not_primes));
	for (int i = 2; i <= 10000;i++) {
		if (!not_primes[i]) {
			for (int k = 2 * i; k <= 10000;k+=i) {
				not_primes[k] = 1;
			}
		}
	}
	int n;
	cin >> n;
	for (int i = 2; i <= n; i++) {
		if (!not_primes[i] && !not_primes[n - i]) {
			cout << i << ' ' << n - i;
			break;
		}
	}
} 

```
<img src="代码截图/屏幕截图 2024-02-19 215325.png" >


代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：



##### 代码

```python
# 
s=input().split('+')
Max=0
for i in s:
    t=i.split('^')
    if(t[0][0]!='0'):
        Max=max(Max,int(t[-1]))
print(f'n^{Max}')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="代码截图/屏幕截图 2024-02-19 221423.png" >



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：



##### 代码

```c++
#include <iostream>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace ::std;

int nums[100001];

int main() {
	memset(nums, 0, sizeof(nums));
	int c=0;
	int t;
	while (cin >> t) {
		nums[t] += 1;
		c = max(c, t);
	}
	int Max = 0;
	for (int i = 1; i <= c; i++) {
		Max = max(Max, nums[i]);
	}
	vector<int> ans;
	for (int i = 1; i <= c; i++) {
		if (nums[i] == Max) {
			ans.push_back(i);
		}
	}
	cout << ans[0];
	for (auto i = ans.begin()+1; i < ans.end(); i++) {
		cout << ' '<<*i;
	}
}

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

<img src="代码截图/屏幕截图 2024-02-19 221613.png" >



## 2. 学习总结和收获

尝试在用c++来做，处理字符串这些麻烦的东西还是用python

寒假的时候没想选数算，没想到闫老师开课了，做了几道寒假pre，学会了字典树

==如果作业题目简单，有否额外练习题目，比如：OJ“数算pre每日选做”、CF、LeetCode、洛谷等网站题目。==





