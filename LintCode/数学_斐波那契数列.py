#斐波那契数列

class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        return self.fib(0, 1, n)

    def fib(self ,a,b,n):
        if n>1:
            return self.fib(a+b,a,n-1)
        return a

if __name__=='__main__':
    n=int(input())
    MySolution=Solution()
    ans=MySolution.fibonacci(n)
    print(ans)