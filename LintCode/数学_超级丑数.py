# 写一个程序来找第 n 个超级丑数。
#
# 超级丑数的定义是正整数并且所有的质数因子都在所给定的一个大小为 k 的质数集合内。
#
# 比如给你 4 个质数的集合 [2, 7, 13, 19], 那么 [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] 是前 12 个超级丑数。

# 1 永远都是超级丑数不管给的质数集合是什么。
# 给你的质数集合已经按照升序排列。
# 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000

# 样例
# 给出 n = 6 和质数集合 [2, 7, 13, 19]。第 6 个超级丑数为 13，所以返回 13 作为结果。


class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        result=[1]
        if n==1:
            return result[0]
        while len(result)<n:
            tempnum=[]
            for i in range(0, len(primes)):
                for j in range(0, len(result)):
                    if primes[i] * result[j] > result[-1]:
                        tempnum.append(primes[i]*result[j])
                        break
            result.append(min(tempnum))
        return result[-1]

if __name__=='__main__':
    #input
    n=int(input())
    primes=list(map(int,input().split(' ')))
    solution=Solution()
    ans=solution.nthSuperUglyNumber(n,primes)
    print(ans)