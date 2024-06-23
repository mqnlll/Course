class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None
flag=0
while 1:
    is_leaves=set()
    def insert(node,val):
        if not node:
            return Node(val)
        if val<node.val and (not node.left or (not node.left.val in is_leaves)):
            node.left=insert(node.left,val)
        else:
            node.right=insert(node.right,val)
        return node


    leaves=[]

    while 1:
        s=input()
        if s=='$':
            flag=1
            break
        if s=='*':
            break
        leaves.append(s)

    root=Node(leaves.pop())
    now=root

    while leaves:
        leave=leaves.pop()
        is_leaves=set(leave)
        for v in leave:
            insert(root,v)

    ans=[]
    def f(node):
        if not node:
            return
        ans.append(node.val)
        f(node.left)
        f(node.right)
    f(root)
    print(''.join(ans))

    if flag:
        break