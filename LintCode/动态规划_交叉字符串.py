#
# 给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成。
#
# 比如 s1 = "aabcc" s2 = "dbbca"
#
#     - 当 s3 = "aadbbcbcac"，返回  true.
#
#     - 当 s3 = "aadbbbaccc"， 返回 false.

#dp[i]表示s1串中数字 dp[j]表示s2串中数字
#利用i或者j中数值

class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False]*(len(s2)+1) for i in range(len(s1)+1)]
        dp[0][0]=True
        for i in range(len(s1)):
            dp[i+1][0]=s1[:i+1]==s3[:i+1]
        for j in range(len(s2)):
            dp[0][j+1]=s2[:j+1]==s3[:j+1]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i]==s3[i+j+1]:
                    dp[i+1][j+1]=dp[i][j+1]
                if s2[j]==s3[i+j+1]:
                    dp[i+1][j+1]|=dp[i+1][j]
        return dp[len(s1)][len(s2)]

if __name__=='__main__':
    solution=Solution()
    s1=input()
    s2=input()
    s3=input()
    ans=solution.isInterleave(s1,s2,s3)
    print(ans)