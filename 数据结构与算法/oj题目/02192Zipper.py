n=int(input())
for z in range(n):
    s1,s2,s=input().split()
    dp=[[0]*(len(s2)+1) for i in range(len(s1)+1)]
    dp[0][0]=1
    for j in range(1,len(s2)+1):
        dp[0][j]=dp[0][j-1] and s2[j-1]==s[j-1]
    for i in range(1,len(s1)+1):
        dp[i][0]=dp[i-1][0] and s1[i-1]==s[i-1]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            dp[i][j]=(s[i+j-1]==s1[i-1] and dp[i-1][j]) or (s[i+j-1]==s2[j-1] and dp[i][j-1])
    if dp[len(s1)][len(s2)]:
        print(f'Data set {z+1}: yes')
    else:
        print(f'Data set {z+1}: no')