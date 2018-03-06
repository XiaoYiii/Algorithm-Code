#扔 n 个骰子，向上面的数字之和为 S。给定 Given n，请列出所有可能的 S 值及其相应的概率。

#example
#input n=1
#output [ [1, 0.17], [2, 0.17], [3, 0.17], [4, 0.17], [5, 0.17], [6, 0.17]]

class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        result=[]
        f=[[0 for i in range(6*n+1)] for i in range(n+1)]

        for i in range(0,7):
            f[1][i]=1/6
        for i in range(2,n+1):
            for j in range(i,6*n+1):
                for k in range(1,7):
                    if j>k:#表明此时可以相加
                        f[i][j]+=f[i-1][j-k] #加上上一次的运算结果概率
                f[i][j]/=6
        for i in range(n,6*n+1):
            result.append((i,f[n][i]))
        return result

if __name__=='__main__':
    solution=Solution()
    n=int(input())
    ans=solution.dicesSum(n)
    print(ans)