

#dp[i][j]表示word1前i个字符到word2前j个字符需要编辑的距离

class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        dp=[[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        dp[0][0]=0
        for i in range(0,len(word1)+1):
            dp[i][0]=i
        for j in range(0,len(word2)+1):
            dp[0][j]=j

        for i in range(0,len(word1)):
            for j in range(0,len(word2)):
                if word1[i]!=word2[j]:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1] + 1, dp[i + 1][j] + 1)
        return dp[len(word1)][len(word2)]

if __name__=="__main__":
    solution=Solution()
    word1=input()
    word2=input()
    ans=solution.minDistance(word1,word2)
    print(ans)