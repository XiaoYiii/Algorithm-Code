






class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n == 1:
            return True
        if n <= 0:
            return False
        temp=True
        while n!=1:
            if n%2!=0:
                temp=False
            n//=2
        return temp

if __name__=='__main__':
    solution=Solution()
    num=int(input())
    ans=solution.checkPowerOf2(num)
    print(ans)