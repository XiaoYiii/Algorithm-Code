# 1， 刻画一个最优解的结构特征
# 2， 递归的定义最优解的值
# 3， 采用自底向上的方法求解最优解的值。

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp=[[0 for j in range(n+1)]for i in range(m+1)]
        dp[1][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if dp[i-1][j]:
                    dp[i][j]+=dp[i-1][j]
                if dp[i][j-1]:
                    dp[i][j]+=dp[i][j-1]
        return dp[m][n]
if __name__=='__main__':
    #input
    m=int(input())
    n=int(input())
    solution=Solution()
    ans=solution.uniquePaths(m,n)
    print(ans)