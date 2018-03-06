#题目:一个人每次只能走一层楼梯或者两层楼梯，问走到第80层楼梯一共有多少种方法。

#解题思路
#假设走到第i-1层需要dp[i-1]中方法，走到第i-2层需要dp[i-2]层方法，走到i层需要dp[i]层方法
#那么有如下关系dp[i]=dp[i-1]+dp[i-2]

def solve(n,dp=[]):
    dp[1],dp[2]=1,2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]

if __name__=='__main__':
    n=int(input())
    dp = [0 for i in range(0, n + 1)]
    print(type(dp))
    solve(n,dp)
    for i in range(1,n+1):
        print(i," ",dp[i])
