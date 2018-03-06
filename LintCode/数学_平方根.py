



class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        low,high=0,x*3
        while low <=high:
            mid=(low+high)//2
            if mid**2<=x and (mid+1)**2>x:
                return mid
            if mid**2<x and (mid+1)**2<=x:
                low=mid+1
            else:
                high=mid-1
        return #表示什么也没有找到



if __name__=='__main__':
    n=int(input())
    mySolution=Solution()
    ans=mySolution.sqrt(n)
    print(ans)