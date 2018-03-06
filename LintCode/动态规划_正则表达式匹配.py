#
# Implement regular expression matching with support for '.' and '*'.
#
# '.'Matches any single character.
# '*' Matches zero or more of the preceding element.

# isMatch("aa","a") → false
#
# isMatch("aa","aa") → true
#
# isMatch("aaa","aa") → false
#
# isMatch("aa", "a*") → true
#
# isMatch("aa", ".*") → true
#
# isMatch("ab", ".*") → true
#
# isMatch("aab", "c*a*b") → true

#aab
#c*a*b
#dp[i][j]

class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        dp=[[False for j in range(0,len(p)+1)]for i in range(0,len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                dp[0][i]=dp[0][i-2]
            for i in range(1,len(s)+1):
                for j in range(1,len(p)+1):
                    if p[j-1]=='*':
                        dp[i][j]=dp[i][j-2]
                        if s[i-1]==p[j-2] or p[j-2]=='.':
                            dp[i][j]|=dp[i-1][j]
                    else:
                        if s[i-1]==p[j-1] or p[j-1]=='.':
                            dp[i][j]=dp[i-1][j-1]
        return dp[len(s)][len(p)]

if __name__=="__main__":
    solution=Solution()
    s=input()
    p=input()
    ans=solution.isMatch(s,p)
    print(ans)