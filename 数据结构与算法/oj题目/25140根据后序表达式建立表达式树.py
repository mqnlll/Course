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