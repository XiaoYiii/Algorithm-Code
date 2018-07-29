# 题目
# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配


# 思路

# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write your code here
        dp=[[False for j in range(0,len(pattern)+1)]for i in range(0,len(s)+1)]
        dp[0][0]=True
        for k in range(1,len(pattern)+1):
            if pattern[k-1]=='*':
                dp[0][k]=dp[0][k-2]# 因为*表示前面字符出现0次或者多次，所以匹配结果和dp[0][k-2]相同
        for i in range(1, len(s) + 1):
            for j in range(1, len(pattern) + 1):
                if pattern[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]# 因为*表示前面字符出现0次或者多次，所以匹配结果和dp[0][k-2]相同
                    if s[i - 1] == pattern[j - 2] or pattern[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                else: #如果是'.'的话
                    if s[i - 1] == pattern[j - 1] or pattern[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[len(s)][len(pattern)]

if __name__=='__main__':
    solution=Solution()
    s='aaa'
    pattern='a*a.a'
    ans=solution.match(s,pattern)
    print(ans)