s=input()
stack=[]
for i in s:
    if i==')':
        tmp=[]
        while 1:
            if stack[-1]=='(':
                stack.pop()
                break
            tmp.append(stack.pop())
        stack+=tmp
        continue
    stack.append(i)
print(''.join(stack))