#题目:假如串s（abcd）、串t（becd），求两者的最长公共子序列
#解题思路
#共有三种情况
#当i与j相等时，那么公共子序列的长度加1
#否则情况下i或j向前走一步，计算当前子序列是否相等，计算当前子序列的最大长度。

#最长公共子序列问题
s=list(input())
t=list(input())
dp=[[0 for x in range(len(t)+1)] for y in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])

print(dp[len(s)][len(t)])


#input abcd becd
#output 3
