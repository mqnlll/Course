depth=0
def f(tree:list,h):
    global depth
    if depth>=len(text):
        return
    if h!=len(text[depth])-1:
        return
    tree.extend([0,[],[]])
    tree[0]=text[depth][-1]
    depth+=1
    f(tree[1],h+1)
    f(tree[2],h+1)
def pre(tree,ans):
    if not tree or tree[0]=='*':
        return
    ans.append(tree[0])
    pre(tree[1],ans)
    pre(tree[2],ans)
def mid(tree,ans):
    if not tree or tree[0]=='*':
        return
    mid(tree[1],ans)
    ans.append(tree[0])
    mid(tree[2],ans)
def suf(tree,ans):
    if not tree or tree[0]=='*':
        return
    suf(tree[1],ans)
    suf(tree[2],ans)
    ans.append(tree[0])
n=int(input())
for _ in range(n):
    tree=[]
    text=[]
    depth=0
    while 1:
        t=input()
        if t=='0':
            break
        text.append(t)
    f(tree,0)
    ans=[]
    pre(tree,ans)
    print(''.join(ans))
    ans=[]
    suf(tree,ans)
    print(''.join(ans))
    ans=[]
    mid(tree,ans)
    print(''.join(ans))
    print()